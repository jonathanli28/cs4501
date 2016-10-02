from django.shortcuts import render
import urllib.request, json
from django.http import JsonResponse

# Create your views here.

def homePageData(request):
    if request.method == 'GET':
        list = []
        urlForLastItem = "http://localhost:8001/api/v1/item/get/"
        urlForLatest = "http://localhost:8001/api/v1/item/getlatest"

        req = urllib.request.Request(urlForLatest)
        ret = urllib.request.urlopen(req).read().decode('utf-8')
        latest = json.loads(ret.read)

        for x in range(0, 3):
            rearNumber = latest["fields"]["pk"]
            requester = urllib.request.Request(urlForLastItem + str(rearNumber - x))
            response = urllib.request.urlopen(requester).read().decode('utf-8')
            bikeItem = json.load(response.read())
            list.append(bikeItem)

        final = { 'bike1' : list[0], 'bike2' : list[1], 'bike3' : list[2] }
        return JsonResponse(final)

def individualItemData(request):
    if request.method == 'GET':
        url = request.path
        urlStr = url.split("/")[5]

        urlForParticularItem = "http://localhost:8001/api/v1/item/get/"
        response = urllib.request.urlopen(urlForParticularItem + urlStr)
        bikeItem = json.loads(response.read)
        return JsonResponse(bikeItem)

def invalidURL(request):
    obj= {}
    obj['status'] = False
    obj['message'] = "Invalid api request"
    return JsonResponse(obj)

