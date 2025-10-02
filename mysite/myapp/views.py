from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "myapp/index.html")

def aboutus(request):
    return render(request, "myapp/aboutus.html")

def services(request):
    return render(request, "myapp/services.html")

def membership(request):
    return render(request, "myapp/membership.html")

def contact(request):
    return render(request, "myapp/contact.html")
