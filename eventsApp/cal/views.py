from django.shortcuts import render
from django.views import generic
from .models import Event

# Create your views here.
def home(request):
    return render(request, 'home.html')

class EventListView(generic.ListView):
    model = Event

class EventDetailView(generic.DetailView):
    model = Event


