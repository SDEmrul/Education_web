from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from myapp.models import *
from .forms import CustomerForm

# Create your views here.
def home(request):
    course=Courses.objects.all()
    return render(request,"index.html",{"C":course})

def about(request):
    about=About.objects.all()
    return render(request,"about.html",{"A":about})

def courses(request):
    course=Courses.objects.all()
    return render(request,"courses.html",{"C":course})

def events(request):
    return render(request,"events.html")



def trainers(request):
    trainer=Trainers.objects.all()
    return render(request,"trainers.html",{"t":trainer})

def contact(request):
    form=CustomerForm()
    if request.method=="post":
        name=request.post.get("name")
        email=request.post.get("email")
        subject=request.post.get("subject")
        message=request.post.get("message")
        obj=Customar()
        obj.name=name
        obj.email=email
        obj.subject=subject
        obj.message=message
        obj.save()

    return render(request,"contact.html",{"F":form})
def signup(request):
   
    if request.method=='POST':
        sname=request.POST.get("n")
        uname=request.POST.get('u')
        uemail=request.POST.get('e')
        upass=request.POST.get('p')
        obj=User()
        obj.first_name=sname 
        obj.username=uname   
        obj.email=uemail
        obj.set_password(upass)
        obj.save()
        return redirect('l')

    return render(request,'signup.html',)
def login(request):
   
    if request.method=='POST':
       if request.method == "POST":
        username = request.POST.get('u')
        password = request.POST.get('p')
    
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display an error message if authentication fails (invalid password)
            
            return redirect('l')
        else:
            # Log in the user and redirect to the home page upon successful login
            auth_login(request, user)
            return redirect('H')
    
    # Render the login page template (GET request)
    return render(request, 'login.html')

