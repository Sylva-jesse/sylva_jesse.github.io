from django.contrib import admin
from django.urls import path
from . views import (
    index, 
    about_us, 
    menu, 
    blog, 
    contact, 
    elements, 
    register,
    login,
    regdone,
    logdone
)

urlpatterns = [
    path('', index, name="index"),
    path('about_us/', about_us, name="about_us"),
    path('menu/', menu, name="menu"),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
    path('elements/', elements, name="elements"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('register/regdone/', regdone, name="regdone"),
    path('login/logdone/', logdone, name="logdone"),
]