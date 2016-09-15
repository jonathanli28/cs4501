from django.core import serializers
from .models import User, BicycleItem
from django.http import HttpResponse
# Create your views here.

def index(request):

    return HttpResponse("Hello, World.\n")

def retrieve_or_modify_user_info(request):
    if request.method == 'GET':
        user = User.user_id(request.GET)
        userJSON = serializers.serialize('json', [ user, ])
        return HttpResponse(userJSON)
    elif request.method == 'POST':
        user = User.user_id(request.GET)
        for key in request:
            user.key = request.POST[key]

def retrieve_or_modify_item_info(request):
    if request.method == 'GET':
        bikeObj = BicycleItem.item_id(request.GET)
        itemJSON = serializers.serialize('json', [ bikeObj, ])
        return HttpResponse(itemJSON)
    elif request.method == 'POST':
        bike = BicycleItem.item_id(request.GET)
        for key in request:
            bike.key = request.POST[key]

def createItem(request):
    bike = BicycleItem
    for key in request:
            bike.key = request.POST[key]



