from django.shortcuts import render
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from myapplication.forms import UserForm, UserProfileForm
from django.core.mail import send_mail
from django.contrib.auth.views import password_reset, password_reset_confirm
from Crypto.Hash import SHA256
from Crypto.Cipher import ARC4

# Create your views here.
from django.http import HttpResponse


def index(request):

    return HttpResponse("Hello, World.\n")

