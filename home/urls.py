from .views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", index, name="home"),
    path("login", signin, name="login"),
    path("signup", signup, name="signup"),
    path("signup/individual_signup", individual_signup, name="individual_signup"),
    path("signup/center_signup", center_signup, name="center_signup"),
    path("logout", signout, name="signout"),
    path("update", addMore, name="addMore"),
    path('search', searchPage.as_view(), name="searchPage"),
    path('center/<slug>', getCenter, name="getCenter"),
    path('book/<slug>', bookCenter, name="bookCenter"),
    path('confirmBooking', confirmBooking, name="confirm"),
]
