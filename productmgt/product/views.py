from multiprocessing import context
from django.shortcuts import render
from .forms import Productform
# Create your views here.
def home(request):
    form = None
    total = 0
    per = 0
    net_total = 0
    if request.method == "POST":
        form = Productform(request.POST)
        p1 = int(form["p1"].value())
        p2 = int(form["p2"].value())
        p3 = int(form["p3"].value())
        p4 = int(form["p4"].value())
        p5 = int(form["p5"].value())
        p6 = int(form["p6"].value())
        p7 = int(form["p7"].value())
        p8 = int(form["p8"].value())
        p9 = int(form["p9"].value())
        p10 = int(form["p10"].value())
        
        total = p1+p2+p3+p4+p5+p6+p7+p8+p9+p10
        print(total)
        # 5%
        per = (total / 100) * 5
        net_total = total - per
    else:
        form = Productform()
    context = {
        'form': form,
        'total': total,
        'per': per,
        'net_total': net_total
    }
    return render(request, "product/home.html", context)

from django.shortcuts import render
from deep_translator import GoogleTranslator

def translator_view(request):
    translation = None
    if request.method == "POST":
        english_word = request.POST.get("word")
        if english_word:
            try:
                translation = GoogleTranslator(source='en', target='ar').translate(english_word)
            except Exception as e:
                translation = f"❌ Error: {e}"

    return render(request, "product/translator.html",)
