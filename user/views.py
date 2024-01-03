from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')
      

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username = username).exists():
                    messages.info(request, 'Username Taken..')
                    return redirect('register')
        elif User.objects.filter(email = email).exists():
                    messages.info(request, 'Email Taken ...')
                    return redirect('register')
        else:
                    user = User.objects.create_user(username = username, password = password,  email = email )
                    user.save()
                    print("user created.")
                    return redirect('login')
    else:
      return render(request, 'register.html')
    

def login(request):
       if request.method == 'POST':
              username = request.POST['username']
              password = request.POST['password']

              user= auth.authenticate(request, username = username, password = password)

              if user is not None:
                     auth.login(request, user)
                     return redirect("/")
              else: 
                     messages.info(request, 'invalid credentials')
                     return redirect('login')
       else:
              return render(request, 'login.html')
       
def logout(request):
       auth.logout(request)
       return redirect('/')

        
       
