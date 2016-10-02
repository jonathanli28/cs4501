from django.shortcuts import render
import urllib.request, json
from django.http import JsonResponse

# Create your views here.

def homePageData(request):
    if request.method == 'GET':
        list = []
        urlForLastItem = "http://localhost:8001/api/v1/item/get/"
        urlForLatest = "http://localhost:8001/api/v1/item/getlatest"
        response = urllib.request.urlopen(urlForLatest)
        latest = json.loads(response.read)

        for x in range(0, 3):
            rearNumber = latest["fields"]["pk"]
            response = urllib.request.urlopen(urlForLastItem + str(rearNumber - x))
            bikeItem = json.load(response.read())
            list.append(bikeItem)

        final = { 'bike1' : list[0], 'bike2' : list[1], 'bike3' : list[2] }
        return JsonResponse(final)

def individualItemData(request):
    if request.method == 'POST':
        itemPK = request.POST.get('item', '')
        urlForParticularItem = "http://localhost:8001/api/v1/item/get/"
        response = urllib.request.urlopen(urlForParticularItem + str(itemPK[0]))
        bikeItem = json.loads(response.read)
        return JsonResponse(bikeItem)