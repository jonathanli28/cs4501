from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/user/get/[0-9]+/?$', views.retrieve_or_modify_user_info),
    url(r'^api/user/modify/[0-9]+/?$', views.retrieve_or_modify_user_info),
    url(r'^api/user/delete/[0-9]+/?$', views.delete_user),
    url(r'^api/user/create/?$', views.create_user),

    url(r'^api/item/get/[0-9]+/?$', views.retrieve_or_modify_item_info),
    url(r'^api/item/modify/[0-9]+/?$', views.retrieve_or_modify_item_info),
    url(r'^api/item/delete/[0-9]+/?$', views.retrieve_or_modify_item_info),
    url(r'^api/item/create/?$', views.retrieve_or_modify_item_info),

    url(r'^api/itemreview/get/[0-9]+/?$', views.retrieve_or_modify_review),
    url(r'^api/itemreview/modify/[0-9]+/?$', views.retrieve_or_modify_review),
    url(r'^api/itemreview/delete/[0-9]+/?$', views.delete_item_review),
    url(r'^api/itemreview/create/?$', views.createItemReview),
    #match all other urls
    url ('', views.invalidURL),
    #url(r'^api/items/(?P[0-9]+)/$', views.retrieve_or_modify_item_info),
    
]