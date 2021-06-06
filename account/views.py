from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login, authenticate, logout as user_logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm

def login(request):
	if request.user.is_authenticated:
		return redirect('core:index')
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			
			user = authenticate(username=username, password=password)
			if user is not None:
				user_login(request, user)
				return redirect('core:index')
	context = {
		'form': form
	}
	return render(request, 'login.html', context)

@login_required
def logout(request):
	user_logout(request)
	return redirect('core:index')

def signup(request):
	if request.user.is_authenticated:
		return redirect('core:index')
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('account:login')
	context = {
		'form': form
	}
	return render(request, 'signup.html', context)