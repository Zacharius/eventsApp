from django.db import models
from django.urls import reverse


# Create your models here

class Event(models.Model):

    #Fields
    title = models.CharField(max_length=100, primary_key=True)
    desc = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    priceText = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.DateTimeField()
    dateText = models.CharField(max_length=150)
    imgLoc = models.CharField(max_length=100, default='default.jpg')
    category = models.CharField(max_length=100, default='default')
    sourceLink = models.CharField(max_length=250, default="eventnear.us")

    class Meta:
        ordering = [ 'date' ]

    def get_absolute_url(self):
        return reverse('event-detail', args=[self.title])

    def __str_(self):
        return self.title 
    
