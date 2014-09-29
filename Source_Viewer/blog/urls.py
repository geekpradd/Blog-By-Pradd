from django.conf.urls import patterns,url
from blog import views
urlpatterns = patterns('' , 
	url(r'^$' , views.home,name='home'),
	url(r'^posts/(?P<post_name>\w+)/$', views.posts, name="posts"),
	url(r'^categories/(?P<cat_name>\w+)/$',views.categories,name="categories"),
	url(r'^add-category/$',views.add_category,name="add_cat"),
	url(r'^categories/(?P<cat_name_url>\w+)/add-post/$', views.add_post,name="add_page"),
	url(r'^register/$',views.register,name="register"),
	url(r'^login/$',views.user_login,name="login"),
	url(r'^logout/$',views.user_logout,name="logout"),
	url(r'^posts/(?P<post_name>\w+)/delete/$', views.delete_post, name="delete-posts"),
	url(r'^posts/(?P<post_name>\w+)/edit/$', views.edit_post, name="edit-posts"),
	url(r'^profile/$',views.user_profile,name="self-profile"),
	url(r'^profile/(?P<user_name>\w+)/$',views.view_profile,name="self-profile"),


)