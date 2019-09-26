from django.db import models

# Create your models here.

class Twitter(models.Model):
    tweet = models.CharField(max_length=300)
    label = models.IntegerField(null=True, blank=True)
    def to_dict(self):
        return {
            'tweet':self.tweet,
            'label':self.label 
        }                                          
