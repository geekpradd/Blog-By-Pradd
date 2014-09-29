from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cat(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class Post(models.Model):
	category = models.ForeignKey(Cat)
	title = models.CharField(max_length=128)
	content = models.CharField(max_length=1000000)
	author = models.CharField(blank=True,max_length=128)
	date = models.CharField(blank=True,max_length=128)
	def __unicode__(self):
		return self.title

class UserProfilec(models.Model):
	#Establish relaationship between custom Fields and main
	users= models.OneToOneField(User)
	#Add fields
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to="profile_images", blank=True)

	#Unicode is used to retireve the name of the class's main property. Especially when we use ForeignKey's
	#It allows us to know which Category is selected
	def __unicode__(self):
		return self.users.username
				