from django.shortcuts import render
from . forms import UserString
# Create your views here.
def home(request):
    user_str_upper = ''
    user_str_len = 0
    sp = 0
    user_str_words = 0
    if request.method == "POST":
        form = UserString(request.POST)
        user_str = form['str'].value()
        user_str_upper = user_str.upper()
        user_str_words = len(user_str.split())
        user_str_len = len(user_str)
        sp = 0
        for i in user_str:
            if i.isspace():
                sp += 1
    else:
        form = UserString()
        
    context = {
        'form': form,
        'user_str_upper': user_str_upper,
        'user_str_len': user_str_len,
        'sp': sp,
        'user_str_words':user_str_words,
    }
    return render(request, "userstring/home.html", context)