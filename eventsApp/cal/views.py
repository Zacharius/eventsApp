from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import Event
from django.db.models import Q

# Create your views here.
def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

    else:
        f = CustomUserCreationForm(request.POST)

    return render(request, "registration/register.html", {'form': f})

def home(request):
    return render(request, 'home.html', {'event_list' : Event.objects.all()[:3] } )

def user_login(request):
    context = {}
    if request.method == "POST":
        return redirect('home')
    else:
        return render(request, "registration/login.html", context)

def success(request):
    pass

def user_logout(request):
    pass

from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def events(request):

    event_list = Event.objects.all()

    if request.GET.__contains__('search'):
        searchParam = request.GET.__getitem__('search');
        event_list = event_list.filter(Q(title__icontains=searchParam) |
                                          Q(desc__icontains=searchParam))

    if request.GET.__contains__('category'):
        catParam = request.GET.__getitem__('category');
        event_list = event_list.filter(category__icontains=catParam)

    if request.GET.__contains__('venue'):
        venueParam = request.GET.__getitem__('venue');
        event_list = event_list.filter(venue__icontains=venueParam)

    if request.GET.__contains__('date'):
        dateParam = request.GET.__getitem__('date');
        try:
            event_list = event_list.filter(date__date=dateParam)
        except:
            pass

    return render(request, 'cal/event_list.html', {'event_list' : event_list} )

class EventListView(generic.ListView):
    model = Event
    paginate_by = 9

    def get_queryset(self):
        event_list = Event.objects.all()

        if self.request.GET.get('search', ''):
            searchParam = self.request.GET.get('search', '')
            event_list = event_list.filter(Q(title__icontains=searchParam) |
                                              Q(desc__icontains=searchParam))

        if self.request.GET.get('category', ''):
            catParam = self.request.GET.get('category', '')
            event_list = event_list.filter(category__icontains=catParam)

        if self.request.GET.get('venue', ''):
            venueParam = self.request.GET.get('venue', '')
            event_list = event_list.filter(venue__icontains=venueParam)

        if self.request.GET.get('date', ''):
            dateParam = self.request.GET.get('date', '')
            try:
                event_list = event_list.filter(date__date=dateParam)
            except:
                pass

        return event_list

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
