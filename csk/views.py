from django.shortcuts import render

from django.http import HttpResponse 
# Create your views here.
def msd(request):
    return render(request,'msd.html')

def raina(request):
    return HttpResponse('<h1><marquee direction="left" scrollamount="30px">Raina Here:The first Indian batsman to hit a century in all three formats of international cricket.</marquee><h1>')