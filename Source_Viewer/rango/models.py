from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=128,unique=True)
	like = models.IntegerField(default=0)
	def __unicode__(self):
		return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title

class UserProfile(models.Model):
    #Main Object that is equal to Django's user module
    user = models.OneToOneField(User)
    #Additional attributes for the user
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to="profile_images", blank=True)

    #Overide for default unicode as we need to register our additional attributes
    def __unicode__(self):
        return self.user.username



    




























