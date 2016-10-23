from django.shortcuts import render
import urllib.request, json
from django.http import JsonResponse

# Create your views here.
modelsApi = "http://models-api:8000/api/v1/"

def homePageData(request):
    if request.method == 'GET':
        list = []
        urlForLastItem = modelsApi + "item/get/"
        urlForLatest = modelsApi + "item/getlatest"
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
        urlForParticularItem = modelsApi + "item/get/"
        requester = urllib.request.Request(urlForParticularItem + pk)
        response = urllib.request.urlopen(requester).read().decode('utf-8')
        bikeItem = json.loads(response)
    return JsonResponse(bikeItem)

def invalidURL(request):
    obj= {}
    obj['status'] = False
    obj['message'] = "Invalid api request"
    return JsonResponse(obj)

def login(request):
    if request.method == 'POST':
        user_id = request.POST.getlist('username')
        passwd = request.POST.getlist('password')

        data = {'username': user_id,
                'passwd': passwd}

        url = modelsApi + 'auth/create/'
        req = urllib.request.urlopen(url, data=json.dumps(data))
        ret = urllib.request.urlopen(req).read().decode('utf-8')
        auth = ret.getlist('auth')

        authvalue = {'auth': auth}

        urlfront = "http://exp-api:8000/api/v1/" + "login"
        req2 = urllib.request.urlopen(url, data=json.dumps(auth))

def logout(request):
    if request.method == 'POST':
        auth = request.POST.getlist('password')

        data = {'auth': auth }

        url = modelsApi + 'auth/delete/'
        req = urllib.request.urlopen(url, data=json.dumps(data))

def createAccount(request):
    if request.method == 'POST':
        username = request.POST.getlist('username')
        first_name = request.POST.getlist('first_name')
        last_name = request.POST.getlist('last_name')
        passwd = request.POST.getlist('password')

        new_account = {'username': username,
                       'first_name': first_name,
                       'last_name': last_name,
                       'passwd': passwd}

        url = modelsApi + 'auth/create/'
        req = urllib.request.urlopen(url, data=json.dumps(new_account))
        ret = urllib.request.urlopen(req).read().decode('utf-8')


        return ret

