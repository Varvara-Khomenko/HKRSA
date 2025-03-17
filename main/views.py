from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'main/HKMSA _ Home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = authenticate(request, username=username, password=password)
            print(user)
            print(user.username)
            print(user.password)
        except:
            messages.error(request, "User Not Found....")
            print("NOT FOUND")
            return render(request, "main/HKMSA _ Login.html", {"message": "Invalid Credentials"})

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            print("INVALID CREDS")
            messages.error(request, "Username or Password does not match...")
            return render(request, "main/HKMSA _ Login.html", {"message": "Invalid Credentials"})
    return render(request, "main/HKMSA _ Login.html")
