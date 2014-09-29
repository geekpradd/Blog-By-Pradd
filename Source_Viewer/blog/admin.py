from django.contrib import admin
from blog.models import Cat, Post
class PageAdmin(admin.ModelAdmin):
	list_display = ( 'category' ,'title'  ,'content','author','date')




admin.site.register(Cat)
admin.site.register(Post, PageAdmin)