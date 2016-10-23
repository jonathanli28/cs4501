from django.shortcuts import render
import urllib.request, json
from django.http import HttpResponseNotFound
from django.http import JsonResponse, HttpResponse
from django.template.defaulttags import register
from .forms import UserSignupForm
from .forms import LogForm
from .forms import CreateListingForm
from django import forms

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
            return JsonResponse(new_user)
            if new_user['status'] is False:
                return render(request, "signuprejected.html")
            else:
                return render(request, "signupsuccess.html")

    else:
        form = UserSignupForm()
    return render(request, "signup.html", {'signup_form': form})


# def signupSplash(request):
#     signup_form = UserSignupForm()
#     if request.method == 'GET':
#         return render(request, 'signup.html', {'signup_form':signup_form, 'next':next})


def loginSplash(request):
    login_form = LogForm()
    if request.method == 'GET':
        return render(request, 'login.html', {'login_form':login_form, 'next':next})


def createlisting(request):
    clisting_form = CreateListingForm()
    if request.method == 'GET':
        return render(request, 'crlisting.html', {'clisting_form':clisting_form, 'next':next})

def invalidURL(request):
    obj= {}
    obj['status'] = False
    obj['message'] = "Invalid api request"
    return JsonResponse(obj)