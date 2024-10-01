from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from .forms import user_form

# Create your views here.
# TODO: catch the unique user name error with proper UI
def sign_up(request: HttpRequest):
    """
    Register a user and redirect to homepageif a form is valid; otherwise, direct the user to fill the form.
    """
    if request.method == "POST":
        form = user_form(request.POST)

        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['user_name'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password'])
            return HttpResponseRedirect("login")

    else:
        form = user_form()

    return render(request, "registration/signup.html", {"form": form})
