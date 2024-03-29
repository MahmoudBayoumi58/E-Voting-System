from django.urls import path
from .views import *

urlpatterns = [
    path('election/create', create_election, name='create_election'),
    path('election/edit/<int:id>/', edit_election, name='edit_election'),
    path('candidate/add', add_candidate, name='add_candidate'),
    path('candidate/edit/<int:id>/', edit_candidate, name='edit_candidate'),
]
