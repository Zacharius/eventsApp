from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .models import Event
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'home.html', {'event_list' : Event.objects.all()[:3] } )

def user_login(request):
    context = {}
    if request.method == "POST":
        pass
    else:
        return render(request, "registration/login.html", context)

def success(request):
    pass

def user_logout(request):
    pass

def events(request):

    event_list = Event.objects.all()

    if request.GET.__contains__('search'):
        searchParam = request.GET.__getitem__('search');
        event_list = event_list.filter(Q(title__icontains=searchParam) |
                                          Q(desc__icontains=searchParam))

    if request.GET.__contains__('category'):
        catParam = request.GET.__getitem__('category');
        event_list = event_list.filter(category__icontains=catParam)

    return render(request, 'cal/event_list.html', {'event_list' : event_list} )

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
