from django.shortcuts import render
from .forms import NumberForm

# Create your views here.

def convert_to_complex(request):
    complex_number = None
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['integer_number']
            complex_number = complex(num, 0)  # Convert integer to complex number
    else:
        form = NumberForm()

    return render(request, 'converter/convert.html', {'form': form, 'complex_number': complex_number})
