from django.db import models
from django.contrib.auth.models import User

class Hackteam(models.Model):
    team_name = models.CharField(max_length=250)
    participants = models.ManyToManyField(User,
                                          related_name='team_participants')
def __str__(self):
        return self.team_name