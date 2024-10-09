from django.urls import path
from . import views

urlpatterns = [
    # TODO: modify blog write for better access control
    path("", views.blog_home, name="blog_home"),
    path("write", views.blog_writing, name="blog_writing"),
    path("<slug:slug>", views.get_post, name="post"),
]
