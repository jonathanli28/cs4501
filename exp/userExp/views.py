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
        user_id = request.POST['username']
        passwd = request.POST['passwd']

        data = {'username': user_id,
                'passwd': passwd}
    
        url = modelsApi + 'auth/create/'
        data = urllib.parse.urlencode(data)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(url, data)
        response =  urllib.request.urlopen(req)
        ret = response.read().decode('utf-8')
        ret = json.loads(ret)
        authvalue = {}
        if(ret['status'] == True):
            authvalue['auth'] = ret['auth']
            authvalue['status'] = True
            authvalue['message'] = "Authenticator successfully obtained"
        else:
            authvalue['status'] = False
            authvalue['message'] = "Authenticator failed to be obtained"
        return JsonResponse(authvalue)

    
def logout(request):
    if request.method == 'POST':
        auth = request.POST['auth']

        data = {'auth': auth }

        url = modelsApi + 'auth/delete/'
        data = urllib.parse.urlencode(data)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(url, data)
        response =  urllib.request.urlopen(req)
        ret = response.read().decode('utf-8')
        ret = json.loads(ret)
        retJSON = {}
        if(ret['status'] == True):
            retJSON['status'] = True
            retJSON['message'] = "Authenticator deleted"
        else:
            retJSON['status'] = False
            retJSON['message'] = "Authenticator failed to be deleted"
        return JsonResponse(retJSON)

def createAccount(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        passwd = request.POST['passwd']
        email = request.POST['email']

        data = {'username': username,
               'first_name': first_name,
               'last_name': last_name,
               'passwd': passwd,
               'email': email}

        url = modelsApi + 'user/create/'
        data = urllib.parse.urlencode(data)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(url, data)
        response =  urllib.request.urlopen(req)
        ret = response.read().decode('utf-8')
        ret = json.loads(ret)
        retJSON = {}
        if(ret['status'] == True):
            retJSON['status'] = True
            retJSON['message'] = "User created"
        else:
            retJSON['status'] = False
            retJSON['message'] = "User failed to be deleted"
        return JsonResponse(retJSON)
        return ret

