from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB limit
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farm_market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)  # 'farmer' or 'buyer'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    products = db.relationship('Product', backref='farmer', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # potatoes, bananas, legumes, etc.
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.String(50), nullable=False)  # e.g., "10 kg", "5 bunches"
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(100), nullable=True)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    farmer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    products = Product.query.order_by(Product.posted_at.desc()).limit(4).all()
    return render_template('index.html', products=products)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password, user_type=user_type)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('auth/register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check email and password.', 'danger')
    
    return render_template('auth/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.user_type == 'farmer':
        products = Product.query.filter_by(farmer_id=current_user.id).all()
        return render_template('farmer/dashboard.html', products=products)
    else:
        return redirect(url_for('market'))

@app.route('/farmer/post', methods=['GET', 'POST'])
@login_required
def post_product():
    if current_user.user_type != 'farmer':
        flash('Only farmers can post products', 'danger')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        # Validate all form fields
        if not all(field in request.form for field in ['name', 'category', 'price', 'quantity']):
            flash('Please fill all required fields', 'danger')
            return redirect(url_for('post_product'))
        
        try:
            # Process file upload
            image = None
            if 'image' in request.files:
                file = request.files['image']
                if file and file.filename != '':
                    if allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        image = filename
                    else:
                        flash('Invalid file type. Allowed: PNG, JPG, JPEG, GIF', 'danger')
                        return redirect(url_for('post_product'))
            
            # Create new product
            new_product = Product(
                name=request.form['name'],
                category=request.form['category'],
                price=float(request.form['price']),
                quantity=request.form['quantity'],
                description=request.form.get('description', ''),
                image=image,
                farmer_id=current_user.id
            )
            
            db.session.add(new_product)
            db.session.commit()
            
            flash('Product posted successfully!', 'success')
            return redirect(url_for('dashboard'))
            
        except ValueError:
            flash('Invalid price format', 'danger')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
    
    return render_template('farmer/post.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}
           
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/market')
def market():
    category = request.args.get('category')
    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()
    
    categories = db.session.query(Product.category).distinct().all()
    return render_template('market/browse.html', products=products, categories=categories)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('market/product.html', product=product)

@app.route('/llm.txt')
def llm_txt():
    return """# llm.txt - Guidance for AI Language Models
User-agent: GPTBot
User-agent: ChatGPT-User
Disallow: /admin/
Disallow: /private/

Allow: /market/
Allow: /product/

Sitemap: https://yourdomain.com/sitemap.xml""", 200, {'Content-Type': 'text/plain'}

@app.errorhandler(413)
def request_entity_too_large(error):
    flash('File too large (max 2MB)', 'danger')
    return redirect(request.url)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()