from django.shortcuts import render
import urllib.request, json
from django.http import JsonResponse

# Create your views here.


def homePageData(request):
    if request.method == 'GET':
        list = []
        urlForLastItem = "http://models-api:8000/api/v1/item/get/"
        urlForLatest = "http://models-api:8000/api/v1/item/getlatest"
        req = urllib.request.Request(urlForLatest)
        ret = urllib.request.urlopen(req).read().decode('utf-8')
        latest = json.loads(ret)
       
        for x in range(0, 3):
            rearNumber = int(latest["pk"])
            requester = urllib.request.Request(urlForLastItem + str(rearNumber - x))
            response = urllib.request.urlopen(requester).read().decode('utf-8')
            bikeItem = json.loads(response)
            list.append(bikeItem)

        final = { 'bike1' : list[0], 'bike2' : list[1], 'bike3' : list[2] }
        
        return JsonResponse(final)

def individualItemData(request, pk):
    if request.method == 'GET':
        urlForParticularItem = "http://models-api:8000/api/v1/item/get/"
        requester = urllib.request.Request(urlForParticularItem + pk)
        response = urllib.request.urlopen(requester).read().decode('utf-8')
        bikeItem = json.loads(response)
    return JsonResponse(bikeItem)

def invalidURL(request):
    obj= {}
    obj['status'] = False
    obj['message'] = "Invalid api request"
    return JsonResponse(obj)

