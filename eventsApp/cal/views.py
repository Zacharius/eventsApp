from django.shortcuts import render
from django.views import generic
from .models import Event
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html', {'events' : Event.objects.all } )

class EventListView(generic.ListView):
   model = Event 
    
class EventDetailView(generic.DetailView):
    model = Event

class searchView(generic.ListView):
    template_name = 'cal/event_list.html'
    
    def get_queryset(self):
        searchParam = self.kwargs['search']
        return Event.objects.filter(Q(title__icontains=searchParam) |
                                    Q(desc__icontains=searchParam))

