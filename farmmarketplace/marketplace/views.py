from django.shortcuts import render
from django.db.models import Sum, F
from .models import Product, Order, Vendor, Sale

def marketplace_view(request):
    # 1. Dashboard Metrics
    # Calculate Total Sales from the database
    total_sales_value = Sale.objects.aggregate(total=Sum('sale_price'))['total'] or 0

    # Count active listings (products)
    active_listings_count = Product.objects.filter(active=True).count()

    # Count pending shipments (orders that are not shipped)
    pending_shipments_count = Order.objects.filter(is_shipped=False).count()

    # Count active vendors
    active_vendors_count = Vendor.objects.filter(active=True).count()

    # 2. Sales Trend Data
    # For a real-world scenario, you would group by date and aggregate sales.
    # For now, let's simulate this with recent data.
    # We will fetch the sales data from the last 7 days.
    from datetime import date, timedelta
    from django.db.models.functions import TruncDay
    
    today = date.today()
    last_7_days = [today - timedelta(days=i) for i in range(7)]
    
    sales_trend = Sale.objects.filter(order__order_date__gte=last_7_days[-1]) \
        .annotate(day=TruncDay('order__order_date')) \
        .values('day') \
        .annotate(total_day_sales=Sum('sale_price')) \
        .order_by('day')
        
    sales_data = [float(item['total_day_sales']) for item in sales_trend]
    sales_labels = [item['day'].strftime('%b %d') for item in sales_trend]

    # 3. Top Products
    # Find the top 3 best-selling products by quantity
    top_products_query = Sale.objects.values('product__name', 'product__price') \
        .annotate(total_quantity=Sum('quantity')) \
        .order_by('-total_quantity')[:3]

    top_products = [
        {'name': item['product__name'], 'price': item['product__price']}
        for item in top_products_query
    ]

    # Pass the dynamic data to the template context
    context = {
        'total_sales': total_sales_value,
        'active_listings': active_listings_count,
        'pending_shipments': pending_shipments_count,
        'active_vendors': active_vendors_count,
        'sales_data': sales_data,
        'sales_labels': sales_labels,
        'top_products': top_products,
    }

    return render(request, 'marketplace/index.html', context)
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

# This is a placeholder for your Django User model
# In a real Django project, you'd import it from django.contrib.auth.models
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# This view handles user registration requests
class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        """
        #Handles new user registration.
        #Expects 'email' and 'password' in the request data.
        """
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Create a new user (this is a placeholder for a real user creation)
            user = User.objects.create_user(email=email, password=password)
            return Response(
                {"message": "User registered successfully."},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

# This view handles user login requests
class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        """
        #Handles user login and authentication.
        #Expects 'email' and 'password' in the request data.
        """
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate the user (placeholder for Django's authenticate function)
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # A token would be generated and sent back to the client here
            return Response(
                {"message": "Login successful.", "token": "your_auth_token_here"},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Invalid credentials."},
                status=status.HTTP_401_UNAUTHORIZED
            )

# This view handles file uploads from authenticated users
class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
       #Handles file upload.
        #Expects a 'file' in the request.FILES.
        """
        uploaded_file = request.FILES.get('file')
        
        if not uploaded_file:
            return Response(
                {"error": "No file uploaded."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Here you would save the file to your desired location
            # Example: YourModel.objects.create(file=uploaded_file, user=request.user)
            # This is a placeholder for the file saving logic
            file_name = uploaded_file.name
            
            return Response(
                {"message": f"File '{file_name}' uploaded successfully."},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )