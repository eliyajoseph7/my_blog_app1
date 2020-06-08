"""music_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from music import views as view
import music


extra_patterns = [
    path('blog-details/<slug:the_slug>', view.blog_info),
    
] 

urlpatterns = [
    path('', view.index),
    path('blog-home', view.blog_home),
    path('test', view.blog_home),
    path('words', view.words),
    path('', include(extra_patterns), name="view_info"),
    path('etv', view.emmanuel_tv),
    path('about-me', view.aboutMe),
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
