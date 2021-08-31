from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),   
    path("addnotes", views.addnotes, name="addnotes"), 
    path("search", views.search, name="search"),
    path("papers", views.paperhome, name="paperhome"),
    path("searchpaper", views.searchpaper, name="searchpaper"),
    path("subjectpapers", views.subjectpapers, name="subjectpapers"),
    path("addpaper", views.addpaper, name="addpaper"),
    path("contact", views.contact, name="contact")
]
