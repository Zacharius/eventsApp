from django.shortcuts import render
from django.views import generic
from .models import Event
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html', {'event_list' : Event.objects.all()[:3] } )

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

class categoryView(generic.ListView):
	#template_name1 = 'cal/event_list.html'

    def get_queryset(self):
    	searchParam = self.kwargs['category']
    	return Event.objects.filter(category__icontains=searchParam)
