from django.contrib import admin
from rango.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
	list_display = ('title' , 'category' , 'url' ,'views')

class CatAdmin(admin.ModelAdmin):
	list_display=('name' , 'like')

admin.site.register(Category , CatAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
