from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^api/v1/homepage', views.homePageData, name = 'homePage'),
        url(r'^api/v1/itempage/(?P<pk>[0-9]+)/?', views.individualItemData, name = 'itemPage'),
        url(r'^api/v1/createaccount/?$', views.createAccount, name = 'createaccountPage'),
        url(r'^api/v1/createitem/', views.createItem, name = 'createitemPage'),
        url(r'^api/v1/login/?$', views.login, name = 'loginPage'),
        url(r'^api/v1/logout/?$', views.logout, name = 'logoutPage'),
        url ('', views.invalidURL),
        ]