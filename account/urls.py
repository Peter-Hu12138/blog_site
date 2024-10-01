from django.urls import path, include
from . import views

# account/login is directed to login.html by "auth"
urlpatterns = [
    # path('account/', views.members, name='members'),
    path("account/", include("django.contrib.auth.urls")),  # default is to look templates in "templates" in an app?
    path("account/signup", views.sign_up, name="signup")
]
