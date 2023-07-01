from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')
def aboutpage(request):
    return render(request,'generator/aboutpage.html')

def password(request):
# Create your views here.
    length=int(request.GET.get('length',8))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get("Uppercase"):
       characters.extend( list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get("Numbers"):
       characters.extend( list('0123456789'))
    if request.GET.get("Special Characters"):
          characters.extend( list('@$_~#&'))
    yourpassword=""
    for i in range(length):
        yourpassword += random.choice(characters)
    return render(request,'generator/password.html',{'password':yourpassword})
