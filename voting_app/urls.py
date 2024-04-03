from django.urls import path
from .views import *

urlpatterns = [
    path('election/create', create_election, name='create_election'),
    path('election/edit/<int:id>/', edit_election, name='edit_election'),
    path('election/details/<int:id>/', election_details, name='election_details'),
    path('candidate/add', add_candidate, name='add_candidate'),
    path('candidate/edit/<int:id>/', edit_candidate, name='edit_candidate'),
    path('vote/add', add_vote, name='add_vote'),
    path('vote/edit/<int:id>/', edit_vote, name='edit_vote'),
    # action can be vote or un-vote
    path('<int:candidateId>/<str:action>/toggle/', vote_toggle, name='toggle_vote'),
]
