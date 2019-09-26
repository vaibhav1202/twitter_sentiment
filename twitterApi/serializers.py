from rest_framework import serializers
from twitterApi.models import Twitter
class TwitterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Twitter
        fields = ('tweet',)
