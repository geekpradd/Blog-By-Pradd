from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import urllib2
# Create your views here.
def index(request):
  context= RequestContext(request)
  dic={"name":"Nerdastic"}
  return render_to_response('Source/home.html',dic,context)

def code(request):
  context= RequestContext(request)
  if request.method == "POST":
    site = request.POST['a']
    if site[0]!='h':
      site= 'http://' + site
    dat = urllib2.urlopen(site)
    val = dat.read()
    dic= {"code":val}
    return render_to_response('Source/code.html',dic,context)
  else:
    return HttpResponseRedirect('/Source/')
