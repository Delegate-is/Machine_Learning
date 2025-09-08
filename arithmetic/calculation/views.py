# add path in urlpatterns list (path('', index),)
# add url to main urls.py 
# create template folder in app folder (calculation)
# create html file in template folder(add another folder with app name(calculation) inside template folder and store html file there(index.html))
# create folder static in app folder(calculation)
# create folder css in static folder
# create css file in css folder(style.css)
# link css file to html file

from django.shortcuts import render
from . forms import CalculationForm
# Create your views here.
def index(request):
    form = None
    answers = None
    if request.method == 'POST':
        form=CalculationForm(request.POST)
        n1 = int(form['n1'].value())
        n2 = int(form['n2'].value())
        add = n1 + n2
        sub = n1 - n2
        mul = n1 * n2
        div = n1 / n2
        answers = {
            'add':add,
            'sub':sub,
            'mul':mul,
            'div':div,
        }
        print(answers)
    context = {
        'form':CalculationForm(),
        'answers':answers
    }
    return render(request, 'calculation/index.html', context)