from django import forms
from blog.models import Cat,Post,UserProfilec
from django.contrib.auth.models import User

class CatForm(forms.ModelForm):
	name = forms.CharField(max_length=128)

	class Meta:
		model = Cat

class PostForm(forms.ModelForm):
	title = forms.CharField(max_length=128 ,help_text='Enter The Title Of The Post',widget=forms.TextInput(attrs={'class' : 'form-control'}))
	content = forms.CharField(max_length=1000000,widget=forms.Textarea(attrs={'class' : 'form-control'}),help_text='Enter The Content')

	class Meta:
		model = Post
		#Exclude the foreign KeyError
		fields = ('title' , 'content')

class UserForm(forms.ModelForm):
	#Override the password widget as by default it
	#uses a text field.Change to password
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username' , 'password', 'email')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfilec
		fields = ('website' , 'picture')
		