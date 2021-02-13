
from django.shortcuts import render,redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Notice
from math import ceil


def home(request):
    return render(request,'home.html')

def team(request):
    return render(request,'team.html')
def notes(request):
    return render(request,'notes.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        contact = Contact(name = name,email = email,msg = msg)
        contact.save()
    return render(request,'contact.html')


def register(request):

    if request.method=="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']

    # Create User
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
    return render(request,'register.html')

def user_login(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.add_message(request, messages.INFO, 'Hello world.')
            return HttpResponseRedirect(reverse('home'))

        else:
            messages.error(request,"failed")
            return render(request,'error.html')
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url="/login")
def bullet(request):
    return render(request,'bulletin.html')

def notice(request):
    notices = Notice.objects.all()
    print(notices)
    n = len(notices)
    nSlides = n // 4 + ceil((n / 4) + (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'notice': notices}
    return render(request,'notice.html',params)
