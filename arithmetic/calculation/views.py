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