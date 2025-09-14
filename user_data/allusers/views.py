from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, "allusers/home.html", context)

def format_number(request):
    formatted = ""
    if request.method == "POST":
        phone = request.POST.get("phone")
        if len(phone) >= 7:
            country = phone[:2]
            area = phone[2:5]
            rest = phone[5:]
            formatted = f"{country}-{area}-{rest}"
    return render(request, "format_number.html", {"formatted": formatted})
