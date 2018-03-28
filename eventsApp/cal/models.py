from django.db import models
from django.urls import reverse


# Create your models here

class Event(models.Model):

    #Fields
    title = models.CharField(max_length=50, primary_key=True)
    desc = models.TextField()
    venue = models.CharField(max_length=50)
    startDate = models.DateTimeField()

    class Meta:
        ordering = [ 'startDate' ]

    def get_absolute_url(self):
        return reverse('event-detail', args=[self.title])

    def __str_(self):
        return self.title 
    
