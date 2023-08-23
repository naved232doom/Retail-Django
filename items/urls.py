from django.urls import path

from . import views

app_name = "items"

urlpatterns = [
    path("", views.browse, name="browse"),
    path("new/", views.new, name="new"),
    path("<int:pk>/", views.details, name="details"),
    path("<int:pk>/delete", views.delete, name="delete"),
    path("<int:pk>/edit", views.edit, name="edit"),
]
