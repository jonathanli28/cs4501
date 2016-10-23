from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.homepageSplash, name='homePageSplash'),
    url(r'^item/(?P<pk>[0-9]+)/?', views.itempageSplash, name='itemPageSplash'),
    url(r'^about', views.aboutSplash, name='aboutSplash'),
    url(r'^signup', views.signupSplash, name='signupSplash'),
    url(r'^login', views.loginSplash, name='loginSplash'),
    url(r'^blist', views.blistSplash, name='blistSplash'),
    url(r'^crlisting', views.createlisting, name='crlisting'),
    url(r'^signuprejected', views.signuprejected, name='signuprejected'),
    url('', views.invalidURL)
    
]