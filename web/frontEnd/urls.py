from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home', views.homepageSplash, name='homePageSplash'),
    url(r'^item', views.itempageSplash, name='itemPageSplash'),
    url(r'^about', views.aboutSplash, name='aboutSplash'),
    url ('', views.invalidURL),
    
]