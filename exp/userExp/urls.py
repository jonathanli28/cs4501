from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^api/v1/homepage', views.homePageData, name = 'homePage'),
        url(r'^api/v1/itempage', views.individualItemData, name = 'itemPage'),
]