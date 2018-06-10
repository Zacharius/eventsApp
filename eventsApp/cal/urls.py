from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from django.urls import path, re_path
from cal.views import user_login, user_logout, success
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('events/' ,views.EventListView.as_view(), name='event-list'),
    path('search/<search>', views.searchView.as_view(), name='event-list'),
    re_path(r'^events/$', views.EventListView.as_view(), name='event-list'),
    path('events/<str:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('category/<category>', views.categoryView.as_view(), name='event-list'),
    url(r'^register/$', views.register, name='register'),
    # path('login/', user_login, name="user_login"),
    # path('success/', success, name="user_success"),
    # path('logout/', user_logout, name="user_logout"),
]
