from django.shortcuts import render,redirect

# Enable user Login and Logout
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages # informs the user if they have successfully logged in or logged out
from . forms import SignUpForm # Allow to create a view for the form created and import it from forms.py

def home(request):
    #Check if logging in
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You're now Logged in!")
            return redirect('home')
        else:
            messages.success(request,"Try Again!")
            return redirect('home')
    else:
        return render(request,'home.html',{})

def logout_user(request):
    """ Handles the logging out of users"""
    logout(request)
    messages.success(request,"You're Logged Out!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
         form = SignUpForm(request.POST)
         if form.is_valid():
             form.save()

             # Authenticate
             username = form.cleaned_data['username']
             password = form.cleaned_data['password1']
             user = authenticate(username=username,password=password)
             # user will be able to login
             login(request,user)
             messages.success(request,"You have successfully Registered!")
             return redirect('home')

    else:
     # User have not registered they want to but have not
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
        #The {'form':form} context dict parse the form into the webpage and we can do something with it 
    return render(request,'register.html',{'form':form})

