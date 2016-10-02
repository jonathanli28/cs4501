from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/user/get/[0-9]+/?$', views.retrieve_or_modify_user_info),
    url(r'^api/v1/user/modify/[0-9]+/?$', views.retrieve_or_modify_user_info),
    url(r'^api/v1/user/delete/[0-9]+/?$', views.delete_user),
    url(r'^api/v1/user/create/?$', views.create_user),

    url(r'^api/v1/item/get/[0-9]+/?$', views.retrieve_or_modify_item_info),
    url(r'^api/v1/item/modify/[0-9]+/?$', views.retrieve_or_modify_item_info),
    url(r'^api/v1/item/delete/[0-9]+/?$', views.delete_item),
    url(r'^api/v1/item/create/?$', views.createItem),

    url(r'^api/v1/itemreview/get/[0-9]+/?$', views.retrieve_or_modify_review),
    url(r'^api/v1/itemreview/modify/[0-9]+/?$', views.retrieve_or_modify_review),
    url(r'^api/v1/itemreview/delete/[0-9]+/?$', views.delete_item_review),
    url(r'^api/v1/itemreview/create/?$', views.createItemReview),
    #match all other urls
    url ('', views.invalidURL),
    #url(r'^api/items/(?P[0-9]+)/$', views.retrieve_or_modify_item_info),
    
]