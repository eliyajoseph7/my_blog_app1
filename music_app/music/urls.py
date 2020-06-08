
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
# from music import views as view

urlpatterns = [
    url(r'^emmanueltv/$', 'music.views.emmanuel_tv', name='etv'),
]