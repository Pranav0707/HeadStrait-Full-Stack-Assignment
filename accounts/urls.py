from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.UserLogin,name="login"),
    path("register/",views.UserRegistration,name="register")
]
