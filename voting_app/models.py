from django.db import models
from user_app.models import Users


# Create your models here.
class Election(models.Model):
    title = models.CharField(max_length=100,  unique=True)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'election')

    def __str__(self):
        return self.name


# class Voter(models.Model):
#     user = models.OneToOneField(Users, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.get_full_name()
#
#
# class ElectionVoters(models.Model):
#     election = models.ForeignKey(Election, on_delete=models.CASCADE)
#     voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
#
#     class Meta:
#         unique_together = ('election', 'voter')
#
#     def __str__(self):
#         return f'{self.voter.user.get_full_name()} can vote for {self.election.title} election'


class Vote(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    voter = models.ForeignKey(Users, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('election', 'voter')

    def __str__(self):
        return f'{self.voter} voted for {self.candidate} in {self.election}'
