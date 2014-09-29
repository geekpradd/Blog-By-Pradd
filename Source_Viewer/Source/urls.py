from django.conf.urls import patterns, url
from Source import views

urlpatterns= patterns('',
                      url(r'^$',views.index,name='main'),
                      url(r'^code/',views.code,name='code'),

                      )




