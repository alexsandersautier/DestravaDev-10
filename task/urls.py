from django.urls import path
from . import views

urlpatterns = [
    path("", views.tasks, name='tasks'),   
    path("finished/", views.finished, name='finished'),   
    path("create/", views.create, name='create'),   
]