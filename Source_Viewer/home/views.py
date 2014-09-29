# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
DATA = "Home Page Of Rango. Rango is a url linker application based on Django. "
HEAD = "Rango By Pradd"
def index(request):
	#Set the main context dictionary to be rendered by the Server
	cons = RequestContext(request)

	#Replace variables from the template

	dic = {"main" : DATA , "head" : HEAD}

	#Render the response
	return render_to_response('home/index.html',dic,cons)
