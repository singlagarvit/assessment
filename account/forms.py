from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'un'}))
	password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'pass'}))

class RegistrationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class': 'un', 'placeholder': 'Username'})
		self.fields['password1'].widget.attrs.update({'class': 'pass', 'placeholder': 'Password'})
		self.fields['password2'].widget.attrs.update({'class': 'pass', 'placeholder': 'Confirm Password'})