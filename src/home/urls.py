from django.urls import path
from .views import *

app_name = "home"


urlpatterns = [
    path("", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("contact/", contact_page, name="contact"),
]
