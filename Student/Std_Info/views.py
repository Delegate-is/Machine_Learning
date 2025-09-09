from django.shortcuts import render
from .forms import StdForm
from .models import StdInfo

# Create your views here.
def index(request):
    if request.method == "POST":
        form = StdForm(request.POST)
        if form.is_valid():
            form.save()
            form = StdForm()
            context ={
                'form': form,
                'msg': "Data saved successfully"
            }
        else:
            form = StdForm(request.POST)
    
    students = StdInfo.objects.all()
    form = StdForm()
    
    context ={
        'form': form,
        'students': students
    }
    return render(request, 'Std_Info/index.html', context)