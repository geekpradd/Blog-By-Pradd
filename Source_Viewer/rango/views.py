from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category, Page 
from rango.forms import CategoryForm, PageForm,UserForm,UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
CONTENT_VAL = "\n\n Django is an awesome python framework for web devs and allows the usage of the MVT and MVC principles. It's kinda like AngularJS except better.\n"
HEADING = "How To Tango With Django"

def decode_url(params):
	return params.replace('_', ' ')
def index(request):
    request.session.set_test_cookie()
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    category_list = Category.objects.order_by('like')[:5]
    HEAD = "Rango - Content Links"
    TITLE = "Rango"

    for category in category_list:
    	category.url = category.name.replace(' ' , '_')[0:]
    	category.url = category.url.replace('rango/' , '')
    	print category.url

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {"categories" : category_list, "head" :HEAD, "title" : TITLE}

	
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    response = render_to_response('rango/index.html', context_dict, context)
    visits = int(request.COOKIES.get('visits',0))

    #Does the cookie last visit exist?Has the user accessed the site?
    if 'last_visit' in request.COOKIES:
        #GET its value
        last_visit = request.COOKIES['last_visit']
        #Get the time and date out of it 
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        #If it's more than a day since...
        if (datetime.now() - last_visit_time).seconds >30:
            #Update visits
            response.set_cookie('visits' , visits+1)
            #Updated time
            response.set_cookie('last_visit' , datetime.now())
    else:
        response.set_cookie('last_visit',datetime.now())
        response.set_cookie('visits' , visits)
    return response

def refresh(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    category_list = Category.objects.order_by('like')[:5]
    HEAD = "Categories - Rango"
    TITLE = HEAD

    for category in category_list:
    	category.url = category.name.replace(' ' , '_')
    	

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {"categories" : category_list , "head" : HEAD , "title" : TITLE}

	
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    
    #Assigning a variable to the response in order to use cookies..YAY
    response= render_to_response('rango/index.html', context_dict, context)

    #Checking whether the number of visits cookie exists or not. If it does 
    #then we take it's value into a variable. If not then we set a default value

    

    return response
def category(request, category_name_url):
	context = RequestContext(request)
	category_name =decode_url(category_name_url)

	context_dict = {"category_name" : category_name , "category_name_url" : category_name_url}


	try:
		category = Category.objects.get(name=category_name)

		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
		context_dict['category'] = category
		print "Success in trying"
	except Category.DoesNotExist:
		pass

	return render_to_response('rango/category.html',context_dict,context)

def add_category(request):
    context = RequestContext(request)

    #Checking whether the submit type is POST or not (becauase the form is submitted on POST)

    if request.method == 'POST':
        #Process the form data
        form = CategoryForm(request.POST)

        #Check the validity
        if form.is_valid():
            #Save the new category to our SQLite 3 Database
            form.save(commit=True)

            #Now load it up on the Index view as the new Category is saved...Easy!

            return index(request)
        else:
            #if containingf errors, print it out to the terminal )(will replace after dev)
            print form.errors

    else:
        #If not post , then display the form to the user.....(As both Post and get are dpne to the same thread unlike PHP)
        form = CategoryForm()

    #Invoked only when NOT SUCCESS
    return render_to_response('rango/add_category.html' , {"form"  :form} , context)
    
def add_page(request,category_name_url):
    context = RequestContext(request)
    cat= decode_url(category_name_url)
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            #Not commiting the changes directly because we have to check wheter the category exists or not
            page = form.save(commit=False)

            try:
                #Searching the database for a category that matches the params.
                category_name = Category.objects.get(name=cat)
                page.category = category_name
            except Category.DoesNotExist:
                #Showing the New Category Page so that the User can add a new category
                return render_to_response('rango/add_category.html', {}, context)

            page.views = 0
            page.save()

            #Now as the page is added, display the category so that the user can view the page
            return category(request,category_name_url)

        else:
            print form.errors
    else:
        form = PageForm()
        return render_to_response('rango/add_page.html', {"category" : cat, "category_name_url" : category_name_url , "form" : form}, context)

def register(request):
    if request.session.test_cookie_worked():
        print "Coooooookkkiee"
        request.session.delete_test_cookie()
    #GET the Context (Browser Data)
    context = RequestContext(request)
    #Setting Up a boolean for registration. False by default, will change and pass it into the template
    registration = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_Form = UserProfileForm(data=request.POST)

        #If both the forms are valid...
        if user_form.is_valid() and profile_Form.is_valid:
            user = user_form.save() #Take a variable for the save instance

            #Hashing the pass into an algorithm and then saving
            user.set_password(user.password)
            user.save()

            #We have to replace the User Class options in UserProfileForm..(As we had to establish a relationship)
            profile = profile_Form.save(commit=False)
            profile.user = user


            #If the Picture is uploaded...
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            #Now as the registration is successful
            registration = True
        #Errors in the form? Print it to the terminal. It'll be shown to the user also using the context
        else:
            print user_form.errors,profile_Form.errors

    #Not a POST? Then display the form to the user by rendering it...
    else:
        user_form = UserForm()
        profile_Form = UserProfileForm()

    #Rendering it now...This method is always invoked..Control Flow is given in the template
    return render_to_response('rango/add_user.html', {"user_form": user_form,"profile_Form" : profile_Form, "registration" : registration} , context)

def user_login(request):
    #Get the context...Yawn
    context = RequestContext(request)

    #Check whether the method is a POST or other (A GET i.e)
    msg=''
    if request.method == "POST":
        #get the username and password from the form.....
        username = request.POST['username']
        password = request.POST['password']

        #Authenticating from our Database using the authenticate method
        user = authenticate(username=username,password=password)
        #Authenticate returns an object when successfull but returns none when nothing is given.We'll use that for control flow
        if user:
            #Checking whether User is active or not (accounts can be disabled)
            if user.is_active:
                #Log the user in and then redirect
                login(request,user)
                return HttpResponseRedirect('/rango/')
            else:
                msg='Your account has been banned. Please create a new account '
                return render_to_response('rango/login.html' , {"msg" : msg} , context)

        #Our user doesn't exist. Prepare a msg for the guy
        else:
            msg = "Invalid User and Password : {0} and {1}. Please create an account or login properly".format(username,password)
            return render_to_response('rango/login.html' , {"msg" : msg} , context)
    else:
        #Serve the data to the template
        return render_to_response('rango/login.html' , {"msg" : msg} , context)
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')
