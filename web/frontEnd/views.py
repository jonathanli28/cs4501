from django.shortcuts import render
import urllib.request, json
from django.http import HttpResponseNotFound

# Create your views here.

def homepageSplash(request):
    if request.method == 'GET':
        urlForExpLayer = "http://exp-api:8001/api/v1/homepage"
        req = urllib.request.Request(urlForExpLayer)
        ret = urllib.request.urlopen(req).read().decode('utf-8')
        latest = json.loads(ret)
        return render(request, "templates/index.html", latest)

def itempageSplash(request, pk):
    if request.method == 'GET':
        urlForExpLayer = "http://exp-api:8001api/v1/itempage/"
        req = urllib.request.Request(urlForExpLayer + pk)
        ret = urllib.request.urlopen(req).read().decode('utf-8')
        latest = json.loads(ret)
        return render(request, "templates/blist.html", latest)

def aboutSplash(request):
    return render(request, "templates/about.html")

def invalidURL(request):
    return HttpResponseNotFound