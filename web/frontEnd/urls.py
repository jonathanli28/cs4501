from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^api/items/(?P[0-9]+)/$', views.retrieve_or_modify_item_info),
    
]