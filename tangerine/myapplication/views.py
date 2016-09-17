from django.core import serializers
from .models import User, BicycleItem
from django.http import HttpResponse
# Create your views here.

def index(request):

    return HttpResponse("Hello, World.\n")
#r'^api/users/(?P<uuid>[^/]+)/$'
def retrieve_or_modify_user_info(request):
    if request.method == 'GET':
        url = request.path
        usrStr = url.split("/")[4]
        user = User.objects.get(userid = usrStr)
        userJSON = serializers.serialize('json', [ user, ])
        return HttpResponse(userJSON)
    elif request.method == 'POST':
        url = request.path
        usrStr = url.split("/")[4]
        user = User.objects.get(userid = usrStr)
        for key in request:
            user.key = request.POST.get(key, False)
        user.save()
        return HttpResponse(status=status.HTTP_201_CREATED)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
def create_user(request):
    
    user = User.objects.create(userid=request.POST.get("userid", False))
    stringster = ""
    for key in request.POST:
        stringster +=key
        setattr(user, key, request.POST.get(key, False))
    user.save()
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



