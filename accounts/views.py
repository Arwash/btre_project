from django.shortcuts import render, redirect
from django.contrib import messages, auth #to import the messages from seettings.py and use it as made in the partial _alerts.html
from django.contrib.auth.models import User
# Create your views here.

def register (request):
    if request.method == 'POST':
        #Get form values and put them in variables
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check if password match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                   messages.error(request, 'The email is being used')
                   return redirect('register')
                else:
                    # Looks good, let's create the user!
                    user = User.objects.create_user(username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)

                    # Then we have to options. Either: login the user after register is done
                    """ auth.login(request,user)
                    messages.success(request, 'You are now logged in')
                    return redirect('index') """

                    # or: give the user a message that they successfully registered, and direct them to login page
                    user.save()
                    messages.success(request, 'You are now register and can login')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render (request, 'accounts/register.html')


def login (request):
     if request.method == 'POST':
         # Get the values and store them in variables
        username = request.POST['username']
        password = request.POST['password']
        
        #Create variable to authenticate the user
        user = auth.authenticate(username=username, password=password)
        
        # Check if user is not Non, that means the user is found in the database by the inserted username and password
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

     else:
        return render (request, 'accounts/login.html')


def logout (request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect ('index')


def dashboard (request):
    return render (request, 'accounts/dashboard.html')
