from django.core import serializers
from .models import User, Authenticator, BicycleItem, ItemReview
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth import hashers
import os
import hmac
# import django settings file
import settings

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
        else:
            userJSON = serializers.serialize('json', [user,])
            temp = json.loads(userJSON)
            temp[0]['status'] = True
            temp[0]['message'] = "Correctly obtained user"
            userJSON = temp[0]           
        return JsonResponse(userJSON)
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
        except User.DoesNotExist:
            user = None
            retJSON['status'] = False
            retJSON['message'] = "There is no user specified"
            retJSON = userJSON
        return JsonResponse(retJSON)

def create_user(request):

    try:
        user = User.objects.get(username = request.POST['username'])
        if(user != None)
            retJSON = {}
            retJSON['status'] = False
            retJSON['message'] = "username already defined in database"
            return JsonResponse(retJSON)

    user = models.User(username=request.POST['username'],                         
        first_name=request.POST['first_name'],                             
        last_name=request.POST['last_name'],                             
        passwd=hashers.make_password(request.POST['passwd']),                                         \
        date_created=datetime.datetime.now()                        
        )

    user.save()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully created user"
    return JsonResponse(retJSON)
    #include error handles later
def delete_user(request):
    url = request.path
    usrStr = url.split("/")[5]
    user = User.objects.get(pk = usrStr)
    user.delete()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully deleted user"
    return JsonResponse(retJSON)

def create_auth(request):
    try:
        user = User.objects.get(username = request.POST['username'])
    except User.DoesNotExist:
        user = None
    if user == None:
        userJSON = {}
        userJSON['status'] = False
        userJSON['message'] = "There is no user specified"
        return JsonResponse(userJSON)
    retJSON = {}
    temp_passwd = hashers.make_password(request.POST['passwd'])
    if(user.passwd == temp_passwd):

        #creating the authenticator
        auth= hmac.new(key = settings.SECRET_KEY.encode('utf-8'), 
            msg = os.urandom(32), digestmod = 'sha256').hexdigest()

        a = models.Authenticator(user_id=request.POST['user_id'],                                                     
            authenticator= auth,                                        
            date_created=datetime.datetime.now()                        
            )
        a.save()
        retJSON['status'] = True
        retJSON['message'] = "Successfully created authenticator"
    else:
        retJSON['status'] = False
        retJSON['message'] = "Failed to create authenticator"
    return JsonResponse(retJSON)

def check_auth(request):
    retJSON = {}
    try:
        a = Authenticator.objects.get(authenticator = request.POST['auth'])
    except Authenticator.DoesNotExist:
        a = None
    if(a == None):
        retJSON['status'] = False
        retJSON['message'] = "There is no Authenticator in db"
        return JsonResponse(retJSON)
    
    if(a.username == request.POST['username']):
        timeDelta = (datetime.datetime.now() - a.date_created).days * 24 * 60
        if(timeDelta > 60 * 2): #set authenticator time to be two hours 
            retJSON['status'] = False
            retJSON['message'] = "Authenticator expired"
        else:
            retJSON['status'] = True
            retJSON['message'] = "Authenticator valid"
    else:
        retJSON['status'] = True
        retJSON['message'] = "Authenticator invalid(mismatch)"
    return JsonResponse(retJSON)

def delete_auth(request):
    retJSON = {}
    try:
        a = Authenticator.objects.get(authenticator = request.POST['auth'])
    except Authenticator.DoesNotExist:
        a = None
    if(a == None):
        retJSON['status'] = False
        retJSON['message'] = "There is no Authenticator in db"
        return JsonResponse(retJSON)
    a.delete()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully deleted auth"
    return JsonResponse(retJSON)




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
        else:
            bikeJSON = serializers.serialize('json', [bike,])
            temp = json.loads(bikeJSON)
            temp[0]['status'] = True
            temp[0]['message'] = "Correctly obtained item"
            bikeJSON = temp[0]
        return JsonResponse(bikeJSON)
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
        else:
            for key in request.POST:
                setattr(bike, key, request.POST.get(key, False))
            bike.save()
            retJSON['status'] = True
            retJSON['message'] = "Successfully modified bike"
        return JsonResponse(retJSON)

def createItem(request):
    bike = BicycleItem.objects.create()
    stringster = ""
    for key in request.POST:
        setattr(bike, key, request.POST.get(key, False))
    bike.save()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully created bike"
    return JsonResponse(retJSON)

def delete_item(request):
    url = request.path
    usrStr = url.split("/")[5]
    bike = BicycleItem.objects.get(pk = usrStr)
    bike.delete()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully deleted bike"
    return JsonResponse(retJSON)

def getlatestitem(request):
    if request.method == 'GET':
        url = request.path
        try:
            bike = BicycleItem.objects.latest('pk')
        except BicycleItem.DoesNotExist:
            bike = None
        if bike == None:
            bikeJSON = {}
            bikeJSON['status'] = False
            bikeJSON['message'] = "There is no bike specified"
        else:
            bikeJSON = serializers.serialize('json', [bike,])
            temp = json.loads(bikeJSON)
            temp[0]['status'] = True
            temp[0]['message'] = "Correctly obtained item"
            bikeJSON = temp[0]
        return JsonResponse(bikeJSON)

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
        else:
            reviewJSON = serializers.serialize('json', [review,])
            temp = json.loads(reviewJSON)
            temp[0]['status'] = True
            temp[0]['message'] = "Correctly obtained review"
        return JsonResponse(reviewJSON)
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
        else:
            for key in request.POST:
                setattr(review, key, request.POST.get(key, False))
            review.save()
            retJSON['status'] = True
            retJSON['message'] = "Successfully modified review"
        return JsonResponse(retJSON)
def createItemReview(request):
    review = ItemReview.objects.create()

    for key in request.POST:
       setattr(review, key, request.POST.get(key, False))
    review.save()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully created review"
    return JsonResponse(retJSON)

def delete_item_review(request):
    url = request.path
    reviewStr = url.split("/")[5]
    review = ItemReview.objects.get(pk= reviewStr)
    review.delete()
    retJSON = {}
    retJSON['status'] = True
    retJSON['message'] = "Successfully deleted bike"
    return JsonResponse(retJSON)


def invalidURL(request):
    obj= {}
    obj['status'] = False
    obj['message'] = "Invalid api request"
    return JsonResponse(obj)


