from django.contrib import admin
from django.urls import path, include
from . import views
admin.site.site_header = "AI Lobby"
admin.site.site_title = "Welcome to AILobby dashboard"
admin.site.index_title = "Dashboard AILobby"
urlpatterns = [
    path('', views.index, name="home"),
    path('index', views.index, name="home"),
    path('contact', views.contact, name="contact"),
    path('projects', views.projects, name="projects"),
    path('events', views.events, name="events"),
    path('events/webinar', views.webinar, name="webinar"),
    path('events/club', views.club, name="club"),
    path('academics', views.academics, name="academics"),
    path('academics/semester', views.semester, name="semester"),

]







