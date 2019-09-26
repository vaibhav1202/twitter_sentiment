from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from twitterApi import views

router = routers.DefaultRouter() 
router.register(r'twitter', views.TwitterViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^accounts/', include('allauth.urls'))
]
