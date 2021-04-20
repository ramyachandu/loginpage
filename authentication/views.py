from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout 
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				auth_login(request, user)
				return redirect('home')
			else:
				print("Invalid username or password.")
		else:
			print("Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="authentication/login.html", context={"login_form":form})

def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('home')
    context['form']=form
    return render(request,'authentication/sign_up.html',context)

def logout_request(request):
	logout(request)
	return redirect('login')

@login_required(login_url='')
def home(request):
    return render(request,'authentication/home.html')