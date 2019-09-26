from django.shortcuts import render
from rest_framework import viewsets
from twitterApi.models import Twitter
from twitterApi.serializers import TwitterSerializer
from twitterApi import twitterApi
from rest_framework.response import Response

# Create your views here.
class TwitterViewSet(viewsets.ModelViewSet):
    queryset = Twitter.objects.all().order_by('-id')
    serializer_class = TwitterSerializer
    def create(self, request, *args, **kwargs):
        super(viewsets.ModelViewSet, self).create(request, *args, **kwargs)
        ob = Twitter.objects.latest('id')
        y = twitterApi.pred(ob)
        return Response({"status": "Success", "Left": y, 'tmp': args})  # Your override
