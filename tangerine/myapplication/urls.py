from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/users/(?P<uuid>[^/]+)/$', views.retrieve_or_modify_user_info),
    url(r'^api/items/(?P<uuid>[^/]+)/$', views.retrieve_or_modify_item_info),
    url(r'^api/items/(?P<uuid>[^/]+)/create/$', views.retrieve_or_modify_item_info),
]