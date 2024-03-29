from django import forms
from rango.models import Page,Category,UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128,help_text='Please Enter The Category Name')
	views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	like = forms.IntegerField(widget=forms.HiddenInput(),initial=0)

	#Inline Class to provide linking to a Model
	class Meta:
		model = Category

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username' , 'password' ,'email')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model =UserProfile
		fields = ('website' , 'picture')

class PageForm(forms.ModelForm):
	def clean(self):
		cleaned_data = self.cleaned_data
		url = cleaned_data.get('url')

		if url and not url.startswith('http://'):
			url = "http://" + url
			cleaned_data['url'] = url
		return cleaned_data
	title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
	url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

			

	class Meta:
        # Provide an association between the ModelForm and a model
		model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
		fields = ('title', 'url', 'views')