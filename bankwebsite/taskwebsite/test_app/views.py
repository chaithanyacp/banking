# Create your views here.
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CustomerForm

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'customerlogin.html')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('test_app:login')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cfnpassword']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken try another")
                return redirect('test_app:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
        else:
            messages.info(request,"Password Not matching")
            return redirect('register')
        return redirect('test_app:login')
    return render(request,"register.html")
def customer_form(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'customerlogin.html')
            messages.info(request, "Application Submitted")
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})
