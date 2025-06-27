from flask import url_for
from datetime import datetime
from app import app, Product

with app.app_context():
    with open('static/sitemap.xml', 'w') as f:
        f.write('''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">''')
        
        # Static pages
        pages = ['index', 'market', 'login', 'register']
        for page in pages:
            f.write(f'''
<url>
    <loc>{url_for(page, _external=True)}</loc>
    <lastmod>{datetime.now().date().isoformat()}</lastmod>
    <changefreq>weekly</changefreq>
</url>''')
        
        # Dynamic product pages
        for product in Product.query.all():
            f.write(f'''
<url>
    <loc>{url_for('product_detail', product_id=product.id, _external=True)}</loc>
    <lastmod>{product.posted_at.date().isoformat()}</lastmod>
</url>''')
        
        f.write('\n</urlset>')