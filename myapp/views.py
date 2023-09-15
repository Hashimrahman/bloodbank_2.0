from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegistrationForm
from .forms import SignupForm
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login





def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = RegistrationForm()
    return render(request, 'myapp/home.html', {'form': form})

def display(request):
    registrations = Registration.objects.all()
    return render(request, 'myapp/display.html', {'registrations': registrations})



def signup(request):
    error_message = None  

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                error_message = "Username already in use. Please choose a different username."
            else:
                user = User.objects.create_user(username=username, password=password)

                login(request, user)

                return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form, 'error_message': error_message})




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
    return render(request, 'login.html')
