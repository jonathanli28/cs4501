from django.core import serializers
from .models import User, BicycleItem, ItemReview
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
            temp = json.loads(userJSON)
            temp[0]['status'] = True
            temp[0]['message'] = "Correctly obtained user"
            userJSON = json.dumps(struct[0])           
        return HttpResponse(userJSON)
    elif request.method == 'POST':
        url = request.path
        usrStr = url.split("/")[5]
        retJSON = {}
        try:
            user = User.objects.get(pk = usrStr)
            userJSON = serializers.serialize('json', [user,])
            for key in request.POST:
                setattr(user, key, request.POST.get(key, False))
            user.save()
            userJSON = serializers.serialize('json', [user,])
            retJSON['status'] = True
            retJSON['message'] = "Successfully modified user"
            retJSON = json.dumps(retJSON)
        except User.DoesNotExist:
            user = None
            retJSON['status'] = False
            retJSON['message'] = "There is no user specified"
            retJSON = json.dumps(userJSON)
            retJSON = {}        
        return HttpResponse(usrStr)
def create_user(request):
    user = User.objects.create()
    stringster = ""
    for key in request.POST:
        setattr(user, key, request.POST.get(key, False))
    user.save()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully created user"
    retJSON = json.dumps(retJSON)
    return HttpResponse(retJSON)
    #include error handles later
def delete_user(request):
    url = request.path
    usrStr = url.split("/")[5]
    user = User.objects.get(pk = usrStr)
    user.delete()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully deleted user"
    return HttpResponse(retJSON)
#url(r'^api/items/(?P<uuid>[^/]+)/$'
def retrieve_or_modify_item_info(request):
    if request.method == 'GET':
        url = request.path
        usrStr = url.split("/")[5] # make sure to check this code
        try:
            bike = BicycleItem.objects.get(pk = usrStr)
        except BicycleItem.DoesNotExist:
            bike = None
        if bike == None:
            bikeJSON = {}
            bikeJSON['status'] = False
            bikeJSON['message'] = "There is no bike specified"
            bikeJSON = json.dumps(bikeJSON)
        else:
            bikeJSON = serializers.serialize('json', [bike,])
            struct = json.loads(bikeJSON)
            struct[0]['status'] = True
            struct[0]['message'] = "Correctly obtained item"
            bikeJSON = json.dumps(struct[0])
        return HttpResponse(bikeJSON)
    elif request.method == 'POST':
        url = request.path
        bikeStr = url.split("/")[5]
        bike = None
        try:
            bike = BicycleItem.objects.get(pk = bikeStr)
        except BicycleItem.DoesNotExist:
            bike = None
        retJSON = {}
        if bike == None:
            retJSON['status'] = False
            retJSON['message'] = "There is no bike specified"
            retJSON = json.dumps(bikeJSON)
        else:
            for key in request.POST:
                setattr(bike, key, request.POST.get(key, False))
            bike.save()
            retJSON['status'] = True
            retJSON['message'] = "Successfully modified bike"
            retJSON = json.dumps(retJSON)
        return HttpResponse(retJSON)

def createItem(request):
    bike = BicycleItem.objects.create()
    stringster = ""
    for key in request.POST:
        setattr(bike, key, request.POST.get(key, False))
    bike.save()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully created bike"
    retJSON = json.dumps(retJSON)
    return HttpResponse(retJSON)

def delete_item(request):
    url = request.path
    usrStr = url.split("/")[5]
    bike = BicycleItem.objects.get(pk = usrStr)
    bike.delete()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully deleted bike"
    retJSON = json.dumps(retJSON)
    return HttpResponse(retJSON)

def retrieve_or_modify_review(request):
    if request.method == 'GET':
        url = request.path
        usrStr = url.split("/")[5] # make sure to check this code
        try:
            review = ItemReview.objects.get(pk = usrStr)
        except BicycleItem.DoesNotExist:
            review = None
        if review == None:
            reviewJSON = {}
            reviewJSON['status'] = False
            reviewJSON['message'] = "There is no review specified"
            reviewJSON = json.dumps(reviewJSON)
        else:
            reviewJSON = serializers.serialize('json', [review,])
            struct = json.loads(reviewJSON)
            struct[0]['status'] = True
            struct[0]['message'] = "Correctly obtained review"
            reviewJSON = json.dumps(struct[0])
        return HttpResponse(reviewJSON)
    elif request.method == 'POST':
        url = request.path
        reviewStr = url.split("/")[5]
        review = None
        try:
            review = ItemReview.objects.get(pk = reviewStr)
        except ItemReview.DoesNotExist:
            review = None
        retJSON = {}
        if review == None:
            retJSON['status'] = False
            retJSON['message'] = "There is no review specified"
            retJSON = json.dumps(reviewJSON)
        else:
            for key in request.POST:
                setattr(review, key, request.POST.get(key, False))
            review.save()
            retJSON['status'] = True
            retJSON['message'] = "Successfully modified review"
            retJSON = json.dumps(retJSON)
        return HttpResponse(retJSON)
def createItemReview(request):
    review = ItemReview.objects.create()

    for key in request.POST:
       setattr(review, key, request.POST.get(key, False))
    review.save()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully created review"
    retJSON = json.dumps(retJSON)
    return HttpResponse(retJSON)

def delete_item_review(request):
    url = request.path
    reviewStr = url.split("/")[5]
    review = ItemReview.objects.get(pk= reviewStr)
    review.delete()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully deleted bike"
    return HttpResponse(retJSON)


def invalidURL(request):
    obj= {}
    obj['status'] = False
    obj['message'] = "Invalid api request"
    json_data = json.dumps(obj)
    return HttpResponse(json_data)


