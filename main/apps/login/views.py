from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"login/index.html")

def success(request):
    if not "name" in request.session:
        messages.error(request,"You must be logged in to access that page")
        return redirect('/')
    else:
        return render(request,"login/success.html")

def logout(request):
    request.session.clear()
    messages.success(request,"Succesfully logged out!")
    return redirect('/')

def register(request):
    if request.method == 'POST':
        validation_return = User.objects.registration_validator(request.POST)
        if "error_messages" in validation_return:
            for value in validation_return["error_messages"].values():
                messages.error(request, value)
            return redirect('/')
        elif "user" in validation_return:
            request.session['user_id'] = validation_return['user'].id
            request.session['name'] = validation_return['user'].first_name
            messages.success(request,"Succesfully registered!")
            return redirect('/success')
        else:
            print("something went wrong")
            return redirect('/')
    else:
        return redirect('/')

def login(request):
    if request.method == 'POST':
        validation_return = User.objects.login_validator(request.POST)
        if validation_return:
            request.session['user_id'] = validation_return['user'].id
            request.session['name'] = validation_return['user'].first_name
            messages.success(request,"Succesfully Logged in!")
            return redirect('/success')
        else:
            messages.error(request, "Invalid Login")
            return redirect('/')
    else:
        return redirect('/')
            
    
