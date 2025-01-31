from django.urls import path
from . import views

urlpatterns=[
    path('infor/', views.get_inform),
]