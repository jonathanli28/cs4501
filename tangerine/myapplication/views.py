from django.core import serializers
from .models import User, BicycleItem
from django.http import HttpResponse
import json
# Create your views here.

def index(request):

    return HttpResponse("Welcome to tangerine.\n")
#r'^api/users/(?P<uuid>[^/]+)/$'
def retrieve_or_modify_user_info(request):
    if request.method == 'GET':
        url = request.path
        usrStr = url.split("/")[5] # make sure to check this code 
        try:
            user = User.objects.get(pk = usrStr)
        except User.DoesNotExist:
            user = None
        if user == None:
            userJSON = {}
            userJSON['status'] = False
            userJSON['message'] = "There is no user specified"
            userJSON = json.dumps(userJSON)
        else:
            userJSON = serializers.serialize('json', [user,])
            struct = json.loads(userJSON)
            struct[0]['status'] = True
            struct[0]['message'] = "Correctly obtained user"
            userJSON = json.dumps(struct[0])           
        return HttpResponse(userJSON)
    elif request.method == 'POST':
        url = request.path
        usrStr = url.split("/")[5]
        user = None
        try:
            user = User.objects.get(pk = usrStr)
        except User.DoesNotExist:
            user = None
        retJSON = {}
        if user == None:
            retJSON['status'] = False
            retJSON['message'] = "There is no user specified"
            retJSON = json.dumps(userJSON)
        else:
            for key in request:
                user.key = request.POST.get(key, False)
            user.save()
            retJSON['status'] = True
            retJSON['message'] = "Successfully modified user"
            retJSON = json.dumps(retJSON)
        return HttpResponse(retJSON)
def create_user(request):
    user = User.objects.create()
    stringster = ""
    for key in request.POST:
        stringster +=key
        setattr(user, key, request.POST.get(key, False))
    user.save()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully created user"
    return HttpResponse(status = 200)
    #include error handles later
def delete_user(request):
    url = request.path
    usrStr = url.split("/")[5]
    user = User.objects.get(userid = usrStr)
    user.delete()
    return HttpResponse(usrStr + "hello")
#url(r'^api/items/(?P<uuid>[^/]+)/$'
def retrieve_or_modify_item_info(request):
    """
    if request.method == 'GET':
        bikeObj = BicycleItem.item_id(request.GET)
        itemJSON = serializers.serialize('json', [ bikeObj, ])
        return HttpResponse(itemJSON)
    elif request.method == 'POST':
        bike = BicycleItem.item_id(request.GET)
        for key in request:
            bike.key = request.POST[key]"""
#r'^api/items/(?P<uuid>[^/]+)/create/$'
def createItem(request):
   """ bike = BicycleItem
    for key in request:
            bike.key = request.POST[key]"""
def invalidURL(request):
    obj= {}
    obj['status'] = False
    obj['message'] = "Invalid api request"
    json_data = json.dumps(obj)
    return HttpResponse(json_data)


