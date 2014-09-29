# Create your views here.
from blog.forms import CatForm, PostForm,UserForm,UserProfileForm
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from blog.models import Cat,Post
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.contrib.auth.models import User
from blog.models import UserProfilec



def home(request):
	
	posts = Post.objects.all()
	for post in posts:
		post.url = post.title.replace(' ', '_')
		post.cat_url = post.category.name.replace(' ' , '_')
		s = post.content.split(' ')
		post.sl =''
		words=0
		try:
			while words<=100:
				post.sl += s[words] + ' '
				words+=1
		except:
			pass
		varx = reversed(posts) #Reverse the list to display the newer items first
	
	cat_list = Cat.objects.all()
	for ca in cat_list:
		ca.url = ca.name.replace(' ','_')
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
	context = RequestContext(request)
    #Load the Template ...
    
	progress = {"title" : "Blog By Pradd" ,"posts" : varx , "cat" : cat_list}
	return render_to_response('blog/home.html',progress,context)

def posts(request,post_name):
	#Get context 
	cat_list = Cat.objects.all()
	context = RequestContext(request)
	name = post_name.replace('_' , ' ')
	for post in cat_list:
		post.url = post.name.replace(' ', '_')
	cont = {"url" : name , "cat" : cat_list , "link" : post_name}
	try:
		post_dic = Post.objects.get(title=name)
		cont['post']=post_dic
		cont['posts'] = varx
	except:
		pass
	

	return render_to_response('blog/post.html', cont, context)

@login_required
def delete_post(request,post_name):
	context = RequestContext(request)
	name = post_name.replace('_', ' ')

	try:
		dic = Post.objects.get(title=name)
		dic.delete()
		msg = "Operation Successfull"
	except:
		msg=" Operation Failed "

	return HttpResponseRedirect('/blog/')
def categories(request,cat_name):
	context = RequestContext(request)
	print cat_name
	cat_list = Cat.objects.all()
	cat_abs = cat_name.replace('_' , ' ')
	context_dic = {"name" : cat_abs,"url":cat_name,"cat" : cat_list}
	for post in cat_list:
		post.url = post.name.replace(' ', '_')
		
	try:
		cat_dic = Cat.objects.get(name=cat_abs)
		pos = Post.objects.filter(category=cat_dic)
		for pot in pos:
			pot.url = pot.title.replace(' ', '_')
		context_dic['category'] = cat_dic
		context_dic['pots'] = pos
	except:
		pass

	return render_to_response('blog/category.html' , context_dic,context)

def add_category(request):
	context = RequestContext(request)

	if request.method == "POST":
		form = CatForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			return home(request)

		else:
			print form.errors
	else:
		form = CatForm()
	cat_list = Cat.objects.all()
	return render_to_response('blog/add_category.html', {"form" : form,"cat":cat_list}, context)

def add_post(request,cat_name_url):
	context = RequestContext(request)

	#Decode the URL into it's name
	cat_name = cat_name_url.replace('_' , ' ')

	if request.method == "POST":
		form = PostForm(request.POST)
		print cat_name
		if form.is_valid():
			post = form.save(commit=False)

			
			try:
				userx = request.user.username
				cat = Cat.objects.get(name=cat_name)
				d = dt.datetime.today().strftime("%d/%m/%Y")
				post.author = userx
				post.category = cat
				post.date = d
				post.save()
			except Cat.DoesNotExist:
				pass

			

			
			return HttpResponseRedirect('/blog/')
		else:
			print form.errors
	else:
		form = PostForm()
		return render_to_response('blog/add_page.html' , {"form" : form,"cat_name" :cat_name,"urls" : cat_name_url} , context)

def register(request):
	#Get context
	context = RequestContext(request)
	registration = False
	#Check HTTP method
	if request.method == "POST":
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			#Set password
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)

			#Set the user instance from our model to the current instance
			profile.users = user	
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			#Save
			profile.save()
			registration=True
		else:
			print user_form.errors,profile_form.errors

	else:
		user_form = UserForm()
		profile_form= UserProfileForm()

	#Render
	return render_to_response('blog/register.html', {"user_form" : user_form , "profile_form" : profile_form , "registration" :registration} , context)
	

def user_login(request):
	cat_list = Cat.objects.all()
	for post in cat_list:
		post.url = post.name.replace(' ', '_')
	context = RequestContext(request)
	msg =''
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/blog/')
			else:
				msg='Your Account has been deactivated'
				return render_to_response('blog/login.html' , {"msg" : msg , "cat" : cat_list}, context)

		else:
			msg="The account with username {0} and pass {1} does not exist. Please login correctly or register".format(username,password)
			return render_to_response('blog/login.html' , {"msg" : msg , "cat" : cat_list}, context)

	else:
		return render_to_response('blog/login.html' , {"msg" : msg , "cat" : cat_list}, context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/blog/')

@login_required
def edit_post(request,post_name):
	#GET the context
	context = RequestContext(request)
	cat_list = Cat.objects.all()
	for post in cat_list:
		post.url = post.name.replace(' ', '_')
	name = post_name.replace('_' , ' ')
	if request.method =="POST":
		new_title = request.POST['title']
		new_content = request.POST['content']
		print "scenario 1"
		
		try:
			newedit = Post.objects.get(title=name)
			newedit.title = new_title
			newedit.content = new_content
			newedit.date = dt.datetime.today().strftime("%d/%m/%Y")
			newedit.save()
		except:
			pass

		return HttpResponseRedirect('/blog/')
		

	else:
		exist=True
		dic = {"exist": exist , "name" : name, "url"  :post_name , "cat" : cat_list}
		
		sin = Post.objects.get(title=name)
		dic['sin'] = sin
		
		
		
		return render_to_response('blog/edit-post.html' ,dic  , context)


@login_required
def user_profile(request):
	context = RequestContext(request)

	cat_list = Cat.objects.all()

	dic = {"cat" : cat_list}
	user = User.objects.get(username=request.user.username)
	dic['userx'] =user
	try:
		#If The Userprofile is present
		up = UserProfilec.objects.get(user=user)

	except:
		up=None


	dic['pr'] = up
	return render_to_response('blog/profile.html' , dic,context)
@login_required
def view_profile(request,user_name):
	context = RequestContext(request)

	cat_list = Cat.objects.all()

	dic = {"cat" : cat_list}
	user = User.objects.get(username=user_name)
	dic['userx'] =user
	try:
		#If The Userprofile is present
		up = UserProfilec.objects.get(user=user)

	except:
		up=None

	print up
	dic['pr'] = up
	return render_to_response('blog/profile.html' , dic,context)
