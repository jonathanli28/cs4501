from django.shortcuts import render
import urllib.request, json
from django.http import HttpResponseNotFound
from django.http import JsonResponse
# Create your views here.

def homepageSplash(request):
    if request.method == 'GET':
        urlForExpLayer = "http://exp-api:8000/api/v1/homepage"
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
        urlForExpLayer = "http://exp-api:8000/api/v1/itempage/"
        req = urllib.request.Request(urlForExpLayer + pk)
        ret = urllib.request.urlopen(req).read().decode('utf-8')
        latest = json.loads(ret)
        return JsonResponse(latest)
       # listME = ['name': latest["bike1"]["fields"]["name"], 'pk': latest["bike1"]["pk"],
        #'description': latest["bike1"]["fields"]["bike_description"]} ];


        #return render(request, "templates/binfo.html", latest)

def aboutSplash(request):
    return render(request, "templates/about.html")

def invalidURL(request):
    obj= {}
    obj['status'] = False
    obj['message'] = "Invalid api request"
    return JsonResponse(obj)