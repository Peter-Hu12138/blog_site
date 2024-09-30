from django.urls import path, include
from . import views

urlpatterns = [
    # path('account/', views.members, name='members'),
    path("account/", include("django.contrib.auth.urls")),  # default is to look templates in "templates" in an app?
]
