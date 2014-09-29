# Create your views here.
import django
from random import randint

x= 0
arr = []
while x<100:
	newt = randint(0,x)
	arr.append(newt)
	x+=1
output = ''
for a in arr:
	output += str(a) + " <br><br>"

def index(req):
	return django.http.HttpResponse("<html>\n <style>body{font-family:'Segoe UI';font-size:21px;margin:50px auto;max-width:700px;}</style> <body> \n Created By GeekPradd Running on Django " + str(django.get_version()) + " \n <a href='../rango'> A Link </a> <br><br>A Random List generated in Python : <br><br> " + output + "</body> </html>")
