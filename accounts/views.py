from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


def UserLogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect("index")
        else:
                messages.info(request,'Username Or Password Is Incorrect!!')


    return render(request,'login.html')

    

def UserRegistration(request):
    # if request.method=="POST":
    #     firstname=request.POST.get("firstname")
    #     lastname=request.POST.get("lastname")
    #     email=request.POST.get("email")
    #     username=request.POST.get("username")
    #     password=request.POST.get("password")

    #     user=User()
    registrationform=RegistrationForm()

    if request.method=="POST":
        registrationform=RegistrationForm(request.POST)
        if registrationform.is_valid():
            registrationform.save()
            messages.success(request,"User Successfuly created")
            return redirect("login")

        else:
            messages.info(request, 'invalid registration details')


    context={"form":registrationform}
    return render(request,"register.html",context)

