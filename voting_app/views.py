from django.http import JsonResponse, Http404

from .models import *
from .forms import ElectionForm, CandidateForm, VoteForm
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
            return redirect('add_election')

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
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _(f'{form.cleaned_data["name"]} Candidate successfully added'))
            return redirect('add_candidate')

    else:
        form = CandidateForm()

    return render(request, 'candidate/add_candidate.html', {'form': form})


@permission_required(['change_candidate'], raise_exception=True)
def edit_candidate(request, id):
    candidate = Candidate.objects.get(id=id)
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            form.save()
            messages.success(request, _(f'{form.cleaned_data["name"]} Candidate successfully edited'))
            return redirect('edit_candidate', id=id)

    else:
        form = CandidateForm(instance=candidate)

    return render(request, 'candidate/edit_candidate.html', {'form': form})


@permission_required(['add_vote'], raise_exception=True)
def add_vote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _(f'Vote successfully added'))
            return redirect('add_vote')

    else:
        form = VoteForm()

    return render(request, 'vote/add_vote.html', {'form': form})


@permission_required(['change_vote'], raise_exception=True)
def edit_vote(request, id):
    vote = Vote.objects.get(id=id)
    if request.method == 'POST':
        form = VoteForm(request.POST, instance=vote)
        if form.is_valid():
            form.save()
            messages.success(request, _(f'Vote successfully edited'))
            return redirect('edit_vote', id=id)

    else:
        form = VoteForm(instance=vote)

    return render(request, 'vote/edit_vote.html', {'form': form})


def get_elections():
    now = timezone.now()
    elections = Election.objects.filter(end_date__gte=now)

    return elections


@login_required
def election_details(request, id):
    voted = False
    voted_candidate_id = 0
    try:
        user = request.user
        election = Election.objects.get(id=id)
        vote = Vote.objects.filter(election=election, voter=user).first()
        if vote:
            voted_candidate_id = vote.candidate.id
            voted = True

        context_data = {
            'election': election,
            'voted': voted,
            'voted_candidate_id': voted_candidate_id
        }

        return render(request, 'election/details.html', context_data)
    except Election.DoesNotExist:
        return redirect('error_404')


@login_required
def vote_toggle(request, candidateId, action):
    try:
        user = request.user
        candidate = Candidate.objects.get(id=candidateId)
        election = candidate.election
        voted = False

        existing_vote = Vote.objects.filter(election=election, voter=user, candidate=candidate).first()
        # vote exists and voter need to un-vote candidate
        if existing_vote and action == 'un-vote':
            existing_vote.delete()
            message = 'Your vote has been successfully removed.'

        # vote exists and voter needs to vote a candidate again
        elif existing_vote and action == 'vote':
            message = 'You already voted this candidate.'

        else:
            # vote doesn't exist and voter tries to un-vote candidate
            if action == 'un-vote':
                message = 'You have not voted yet to un-vote candidate'
            else:
                # vote doesn't exist and voter tries to vote
                try:
                    Vote.objects.create(election=election, voter=user, candidate=candidate)
                    message = 'Your vote has been successfully recorded.'
                    voted = True
                except:
                    # voter already voted and tried to vote another candidate
                    message = 'You can not vote 2 candidate in same election'

        vote_count = candidate.vote_set.count()
        return JsonResponse({'voted': voted, 'vote_count': vote_count, 'message': message})

    except Exception as ex:
        message = str(ex)
        return JsonResponse({'message': message}, status=500)
