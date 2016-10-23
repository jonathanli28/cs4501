from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^api/v1/homepage', views.homePageData, name = 'homePage'),
        url(r'^api/v1/itempage/(?P<pk>[0-9]+)/?', views.individualItemData, name = 'itemPage'),
        url(r'^api/v1/validatelogin/', views.login, name = 'itemPage'),
        url(r'^api/v1/validatelogout/', views.logout, name = 'itemPage'),
        url(r'^api/v1/createaccount/', views.createAccount, name = 'itemPage'),
        url ('', views.invalidURL),
        ]