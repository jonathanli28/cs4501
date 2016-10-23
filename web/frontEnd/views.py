from django.shortcuts import render
import urllib.request, json
from django.http import HttpResponseNotFound
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.defaulttags import register
from .forms import UserSignupForm
from .forms import LogForm
from .forms import CreateListingForm
from django import forms
from django.core.urlresolvers import reverse

baseApi = "http://exp-api:8000/api/v1/"

def get_item(dictionary, key):
    return dictionary.get(key)

def homepageSplash(request):
    if request.method == 'GET':
        urlForExpLayer = baseApi + "homepage"
        req = urllib.request.Request(urlForExpLayer)
        ret = urllib.request.urlopen(req).read().decode('utf-8')

        latest = json.loads(ret)
        #return JsonResponse(latest["bike2"]["fields"])
       
        listME = [{'name': latest["bike1"]["fields"]["name"], 'pk': latest["bike1"]["pk"],
        'description': latest["bike1"]["fields"]["bike_description"]},
         {'name': latest["bike2"]["fields"]["name"], 'pk': latest["bike2"]["pk"],
         'description': latest["bike2"]["fields"]["bike_description"]}, 
        {'name': latest["bike3"]["fields"]["name"], 'pk': latest["bike3"]["pk"],
        'description': latest["bike3"]["fields"]["bike_description"]}]
        
        context = {"list":listME}
        
        return render(request, "index.html", context)

def itempageSplash(request, pk):
    if request.method == 'GET':
        urlForExpLayer = baseApi + "itempage/"
        req = urllib.request.Request(urlForExpLayer + pk)
        ret = urllib.request.urlopen(req).read().decode('utf-8')
        latest = json.loads(ret)
        #return JsonResponse(latest)
        listME = {'name': latest["fields"]["name"], 
        "bike_style": latest["fields"]["bike_style"],
        "brake_style": latest["fields"]["brake_style"],
        "color": latest["fields"]["color"],
        "frame-material": latest["fields"]["frame_material"],
        "speeds": latest["fields"]["speeds"],
        "package_height": latest["fields"]["package_height"],
        "shipping_weight": latest["fields"]["shipping_weight"],
        "wheel_size": latest["fields"]["wheel_size"],
        "bike_description": latest["fields"]["bike_description"],
        "average_star_rating": latest["fields"]["average_star_rating"]
        }
        #'description': latest["bike1"]["fields"]["bike_description"]} ];

        context = {"bicycle":listME}

        return render(request, "binfo.html", context)

def aboutSplash(request):
    return render(request, "about.html")
#requests.COOKIES.get(auth)
def blistSplash(request):
    return render(request, "blist.html")

def signuprejected(request):
    return render(request, "signuprejected.html")


def signupSplash(request):
    if request.method == "POST":
        # return HttpResponse(request.POST)
        form = UserSignupForm(request.POST)
        if form.is_valid():
            
            data = {'username': form.cleaned_data['username'],
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'passwd': form.cleaned_data['password1'],
                    'email': 'monkey@virginia.edu'}

            url = baseApi+ 'createaccount'
            data = urllib.parse.urlencode(data)
            data = data.encode('utf-8') # data should be bytes
            req = urllib.request.Request(url, data)
            response =  urllib.request.urlopen(req)
            ret = response.read().decode('utf-8')
            new_user = json.loads(ret)
            if new_user['status'] is False:
                return render(request, "signuprejected.html")
            else:
                return render(request, "signupsuccess.html")

    else:
        form = UserSignupForm()
    return render(request, "signup.html", {'signup_form': form})


def loginSplash(request):
    login_form = LogForm
    next = reverse('homePageSplash') or request.GET.get('next')
    if request.method == 'GET':
        return render(request, 'login.html', {'login_form':login_form, 'next':next})
    f = LogForm(request.POST)
    if not f.is_valid():
        # bogus form post, send them back to login page and show them an error
        return render(request, 'login.html', {'login_form':login_form, 'next':next})
    username = f.cleaned_data['username']
    passwd = f.cleaned_data['passwd'] # need to check this
    
    data = {'username': username,
            'passwd': passwd}

    url = baseApi+ 'login'
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8') # data should be bytes
    req = urllib.request.Request(url, data)
    response =  urllib.request.urlopen(req)
    ret = response.read().decode('utf-8')
    resp = json.loads(ret)

    if not resp or not resp['status']:
        # couldn't log them in, send them back to login page with error
        return render(request, 'login.html', {'login_form':login_form, 'next':next, 'login_message': 'login failed'})
    # logged them in. set their login cookie and redirect to back to wherever they came from
    authenticator = resp['auth']
    response = HttpResponseRedirect(next)
    response.set_cookie("auth", authenticator)
    return response
"""
def login_required(f):
    def wrap(request, *args, **kwargs):
        # try authenticating the user
        user = _validate(request)
        # failed
        if not user:
            # redirect the user to the login page
            return HttpResponseRedirect(reverse('login')+'?next='+current_url)
        else:
            return f(request, *args, **kwargs)
    return wrap
"""

def createlisting(request):
    clisting_form = CreateListingForm()
    next = reverse('homePageSplash')
    auth = request.COOKIES.get('auth')
    if not auth:
      # handle user not logged in while trying to create a listing
      return HttpResponseRedirect(reverse("login") + "?next=" + reverse("crlisting"))
    if request.method == 'GET':
        return render(request, 'crlisting.html', {'clisting_form':clisting_form, 'next':next})

    f = CreateListingForm(request.POST)
    if not f.is_valid():
        return render(request, 'crlisting.html', {'clisting_form':clisting_form, 'next':next})

    #make API call to check authenticator 


    name = f.cleaned_data['name']
    bike_style = f.cleaned_data['bike_style']
    brake_style = f.cleaned_data['brake_style']
    color = f.cleaned_data['color']
    frame_material = f.cleaned_data['frame_material']
    speeds = f.cleaned_data['speeds']
    package_height = f.cleaned_data['package_height']
    shipping_weight = f.cleaned_data['shipping_weight']
    wheel_size = f.cleaned_data['wheel_size']
    bike_description = f.cleaned_data['bike_description']


    data = {"picture": "",
            "name": name,
            "bike_style": bike_style,
            "brake_style": brake_style,
            "color": color,
            "frame_material": frame_material,
            "speeds": speeds,
            "package_height": package_height,
            "shipping_weight": shipping_weight,
            "wheel_size": wheel_size,
            "bike_description": bike_description,
            "auth": auth
            }

    url = baseApi+ 'createitem'
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8') # data should be bytes
    req = urllib.request.Request(url, data)
    response =  urllib.request.urlopen(req)
    ret = response.read().decode('utf-8')
    resp = json.loads(ret)


    if resp and not resp['status']:
        # exp service reports invalid authenticator -- treat like user not logged in
        return HttpResponseRedirect(reverse('homePageSplash')+ "?next=" + reverse("crlisting"))
     
    return render("listing_success.html", {'clisting_form':clisting_form, 'next':next, 'list_message':"item successfully created"})

def logout(request):
    url = baseApi + "api/v1/logout"

    auth = request.COOKIES.get('auth')
    request.delete_cookie(key = auth)
    authpass = {'auth': auth}

    data = urllib.parse.urlencode(authpass)
    req = urllib.request.Request(url, data)

    response =  urllib.request.urlopen(req)
    ret = response.read().decode('utf-8')
    resp = json.loads(ret)

    return resp



def invalidURL(request):
    obj= {}
    obj['status'] = False
    obj['message'] = "Invalid api request"
    return JsonResponse(obj)