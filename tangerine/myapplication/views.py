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
    return HttpResponse("Hello, world.")

def login(request):
    auth_logout(request)
    state = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user: # is not None:
            if user.is_active:
                auth_login(request, user)
                if(user.id ==1 and user.is_staff==False):
                  user.is_staff = True
                  user.save()

                return HttpResponseRedirect(reverse('myapplication.views.home'))
            else:
                state = "User is currently suspended"
                return render(request, "myapplication/login.html", {'state': state})

        else:
            print("Bad login credentials")
            state = "Invalid Login"
            return render(request, "myapplication/login.html", {'state': state})
    else:
        return render(request, "myapplication/login.html")
        #return render(request, "myapplication/login.html")
        #return render(request, "myapplication/login.html", {'redirect_to': next})

@login_required
def logout(request):
    auth_logout(request)
    return render(request, "myapplication/logout.html")
    #return HttpResponseRedirect(settings.LOGIN_URL)

def index(request):
  return render(request, 'myapplication/index.html', None)

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            key = user.username.encode('utf-8')
            real_key = SHA256.new(key).hexdigest()


            cleartextpass = user.password
            # hash_key = SHA256.new(str.encode(user.password)).hexdigest()
            # # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            """
            if user.id == 3:
              user.is_staff = True
            """
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.key = str.encode(real_key)

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            email_subject = 'Account Confirmation'
            email_body = "Thanks for creating an account with SafeCollab. Your username is: %s and your passsword is: %s. Keep your information safe!" %(user.username, cleartextpass)

            send_mail(email_subject, email_body, 'group27emaildjango@gmail.com', [user.email], fail_silently=False)

            # Now we save the UserProfile model instance.
            # profile.key = hash_key
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'myapplication/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )