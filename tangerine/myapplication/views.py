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
    user = User.userid(usrStr)#place holder to get user id 
    userJSON = serializers.serialize('json', [ user, ])
    return HttpResponse(userJSON)
    #elif request.method == 'POST':
     #   user = User.user_id(request.GET)
      #  for key in request:
       #     user.key = request.POST[key]
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



