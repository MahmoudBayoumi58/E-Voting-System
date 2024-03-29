from .models import *
from .forms import ElectionForm, CandidateForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


# Create your views here.

@permission_required(['add_election'], raise_exception=True)
def create_election(request):
    if request.method == 'POST':
        form = ElectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _(f'{form.cleaned_data["title"]} Election successfully created'))
            form = ElectionForm()
            return render(request, 'election/add_election.html', {'form': form})

    else:
        form = ElectionForm()

    return render(request, 'election/add_election.html', {'form': form})


@permission_required(['change_election'], raise_exception=True)
def edit_election(request, id):
    election = Election.objects.get(id=id)
    if request.method == 'POST':
        form = ElectionForm(request.POST, instance=election)
        if form.is_valid():
            form.save()
            messages.success(request, _(f'{form.cleaned_data["title"]} Election successfully edited'))
            return redirect('edit_election', id=id)

    else:
        form = ElectionForm(instance=election)

    return render(request, 'election/edit_election.html', {'form': form})


@permission_required(['add_candidate'], raise_exception=True)
def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _(f'{form.cleaned_data["name"]} Candidate successfully added'))
            form = CandidateForm()
            return render(request, 'candidate/add_candidate.html', {'form': form})

    else:
        form = CandidateForm()

    return render(request, 'candidate/add_candidate.html', {'form': form})


@permission_required(['change_candidate'], raise_exception=True)
def edit_candidate(request, id):
    candidate = Candidate.objects.get(id=id)
    if request.method == 'POST':
        form = CandidateForm(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            messages.success(request, _(f'{form.cleaned_data["name"]} Candidate successfully edited'))
            return redirect('edit_candidate', id=id)

    else:
        form = CandidateForm(instance=candidate)

    return render(request, 'candidate/edit_candidate.html', {'form': form})


def get_elections(user):
    elections = []
    if user.is_authenticated:
        voter = []
        if voter:
            now = timezone.now()
            elections = Election.objects.filter(end_date__gte=now)

    return elections


@login_required
def get_election_details(request, pk):
    election = Election.objects.filter(pk=pk)
    return election
