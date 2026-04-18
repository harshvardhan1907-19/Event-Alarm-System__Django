"""
URL configuration for alarmProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from alarmApp.views import add_event, event_list, events_json, play_song

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', add_event, name='add_event'),
    path('', event_list, name='index'),
    path('events-json/', events_json, name='events_json'),
    path('play/', play_song),
]
