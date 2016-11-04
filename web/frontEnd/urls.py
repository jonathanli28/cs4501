from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.homepageSplash, name='homePageSplash'),
    url(r'^item/(?P<pk>[0-9]+)/?', views.itempageSplash, name='itemPageSplash'),
    url(r'^about', views.aboutSplash, name='aboutSplash'),
    url(r'^signup', views.signupSplash, name='signupSplash'),
    url(r'^login', views.loginSplash, name='loginSplash'),
    url(r'^crlisting', views.createlisting, name='crlisting'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^search', views.searchSplash, name='search'),
    url(r'^searchHeader', views.searchSplash, name='searchHeader'),
    url('', views.invalidURL)
    
]