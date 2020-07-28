from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    return render(request, "index.html", {})

def about_us(request):
    return render(request, "02_about_us.html", {})

def menu(request):
    return render(request, "03_menu.html", {})

def blog(request):
    return render(request, "04_blog.html", {})

def contact(request):
    return render(request, "05_contact.html", {})

def elements(request):
    return render(request, "06_elements.html", {})

def register(request):
    return render(request, "register.html", {})

def login(request):
    return render(request, 'login.html', {})

def regdone(request):
    regobj = models.Register()

    name = request.POST.get('name')
    mail = request.POST.get('mail')
    phone = request.POST.get('phone')
    psw = request.POST.get('psw')
    pswr = request.POST.get('pswr')
    

    # for register
    regobj.name = name
    regobj.mail = mail
    regobj.phone = phone
    regobj.psw = psw
    regobj.pswr = pswr
    regobj.save()

    return render(request, 'regdone.html' )


def logdone(request):
    regobj = models.Register()


    lmail = request.POST.get('lmail')
    lpsw = request.POST.get('lpsw')
    

    # for login
    mail = regobj.name
    psw = regobj.psw


    if lmail == mail:
        return render(request, 'regdone.html' )
    else:
        return render(request, 'sorry.html')