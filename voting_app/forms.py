from django import forms
from .models import *


class ElectionForm(forms.ModelForm):

    class Meta:
        model = Election
        fields = ['title', 'description', 'start_date', 'end_date']


class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ['election', 'name', 'party', 'image']


class VoteForm(forms.ModelForm):

    class Meta:
        model = Vote
        fields = ['election', 'voter', 'candidate']
