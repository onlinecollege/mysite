from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("library/<str:title>", views.library, name="library"),
    path("search", views.search, name="search"),
    path("add", views.add, name="add"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("guide", views.guide, name="guide"),
    path("allpapers", views.allpapers, name="allpapers"),
    path("allpapers/<str:subject>", views.subjectpapers, name="subjectpapers"),
    path("papers/<int:paper_id>", views.papers, name="papers"),
]
