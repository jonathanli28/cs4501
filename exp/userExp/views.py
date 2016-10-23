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
            retJSON['message'] = "User failed to be created"
        return JsonResponse(retJSON)
        
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
            authvalue['message'] = ret['message']
        else:
            authvalue['status'] = False
            authvalue['message'] = ret['message']
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

#make two calls to model layer, one for auth and one for item creation
def createItem(request):
    retJSON = {}

    auth = request.POST['auth']

    name = request.POST['name']
    bike_style = request.POST['bike_style']
    brake_style = request.POST['brake_style']
    color = request.POST['color']
    frame_material= request.POST['frame_material']
    speeds = request.POST['speeds']
    package_height = request.POST['package_height']
    shipping_weight = request.POST['shipping_weight']
    wheel_size = request.POST['wheel_size']
    bike_description = request.POST['bike_description']
    average_star_rating = request.POST['average_star_rating']

    data = {'auth':auth}
    url = modelsApi + 'auth/check/'
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8') # data should be bytes
    req = urllib.request.Request(url, data)
    response =  urllib.request.urlopen(req)
    ret = response.read().decode('utf-8')
    ret = json.loads(ret)
    #if Authentication is successful, then stuff everything in and send
    #to create item call in models layer
    if(ret['status'] == True):
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
                "average_star_rating": average_star_rating,
                "bike_description": bike_description
                }

        url = modelsApi + 'item/create/'
        data = urllib.parse.urlencode(data)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(url, data)
        response =  urllib.request.urlopen(req)
        ret = response.read().decode('utf-8')
        ret = json.loads(ret)

        if(ret['status'] == True):
            retJSON['status'] = True
            retJSON['message'] = "Item created"
        else:
            retJSON['status'] = False
            retJSON['message'] = "Item failed to be created"
    else:
        retJSON['status'] = False
        retJSON['message'] = "Authentication failure"
    return JsonResponse(retJSON)


    return JsonResponse(retJSON)
