from django import forms
from .models import Blog, ContactProfile, Portfolio
#Se importan librerias de Jango.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#se crea la clase contactForm.
class ContactForm(forms.ModelForm):
   #se llevan a cabo parametros para el diseño.
	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Message..',
			'rows': 6,
			}))
	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message')
#Se crea la clase BlogForm con parametros dentro de la misma 
class BlogForm(forms.ModelForm):
   #se llevan a cabo parametros para el diseño.
	author = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Author name..',
			}))
	name = forms.CharField(max_length=200, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	description = forms.CharField(max_length=500, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Description..',
			}))
	body = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Body Info..',
			}))
	image = forms.ImageField()
#Se coloca la clase meta junto al modelo y los fields.
	class Meta:
		model = Blog
		fields = ('author', 'name', 'description','body','image')


class ReviewForm(forms.ModelForm):
   #se llevan a cabo parametros para el diseño.
	author = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Author name..',
			}))
	name = forms.CharField(max_length=200, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	description = forms.CharField(max_length=500, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Description..',
			}))
	body = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Body Info..',
			}))
	image = forms.ImageField()
#Se coloca la clase meta junto al modelo y los fields.
	class Meta:
		model = Portfolio
		fields = ('author', 'name', 'description','body','image')
#Se crea la clase CreateUserForm.
class CreateUserForm(UserCreationForm):
	#Se coloca la clase meta junto al modelo y los fields.
	class Meta:
		model = User
		fields= ['username','email','password1','password2']