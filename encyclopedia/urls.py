from django.urls import path
from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/add/", views.add, name="add"),
    path("wiki/edit/", views.edit, name="edit"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/random_page/", views.random_page, name="random_page"),
    path("wiki/save/", views.save, name="save"),
    path("wiki/search/", views.search, name="search")
    ]
