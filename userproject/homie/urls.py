from django.contrib import admin
from django.urls import path,include
from homie import views
urlpatterns = [
    path("",views.index,name="homie"),
    path("login",views.loginUser,name="login"),
    path("logout",views.logoutUser,name="logout")
]
