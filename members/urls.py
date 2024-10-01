"""
all urls affiliated with members
"""
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/inventory', views.detailed_member_inventory, name='member_inventory'),
    path('members/details/<int:id>', views.details, name='details'),
]
