from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/users/get/[0-9]+/?$', views.retrieve_or_modify_user_info),
    url(r'^api/users/modify/[0-9]+/?$', views.retrieve_or_modify_user_info),
    url(r'^api/users/delete/[0-9]+/?$', views.delete_user),
    url(r'^api/users/create$', views.create_user),
    url(r'^api/items/get/[0-9]+/?$', views.retrieve_or_modify_item_info),
    url(r'^api/items/modify/[0-9]+/?$', views.retrieve_or_modify_item_info),
    url(r'^api/items/delete/[0-9]+/?$', views.retrieve_or_modify_item_info),
    url(r'^api/items/create/?$', views.retrieve_or_modify_item_info),

    #match all other urls
    url ('', views.invalidURL),
    #url(r'^api/items/(?P[0-9]+)/$', views.retrieve_or_modify_item_info),
    
]