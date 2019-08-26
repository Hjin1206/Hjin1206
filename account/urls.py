from django.urls import path
from account import views

urlpatterns =[
    path("login/",views.login),
    path("loginlogic/",views.loginlogic),
    path("regist/", views.regist),
    path("registlogic/", views.registlogic),
    path("home/", views.home),
]