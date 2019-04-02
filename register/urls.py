from django.contrib import admin
from django.urls import path ,re_path,include
from django.views.generic import RedirectView
from . import views
app_name = "register"
urlpatterns = [
    re_path(r'^$',views.index,name = "index"),
    re_path(r'^(?P<event_name>[0-9A-Za-z._%+-]+)submit$',views.submit,name = "submit"),
    re_path(r'^feedback',views.feedback,name="feedback"),
    re_path(r'[0-9A-Za-z._%+-]+',views.error404,name="error404")
]