from django.shortcuts import render
from .models import Slider
# Create your views here.
def index(request):
    
    sliders = Slider.objects.all()
    context = {
        'Sliders' : sliders,
    }
    return render(request,'index.html',context)