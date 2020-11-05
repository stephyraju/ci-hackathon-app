from django.db import models
from hackathon.models import HackTeam, Hackathon
from django.contrib.auth.models import User


class Team_Members(models.Model):

    class Meta:
        verbose_name_plural = "Team_Members"

    name = models.CharField(max_length=30, null=True, blank=True, unique=True)

    def __str__(self):  
        return self.name


class Teams(models.Model):

    class Meta:
        verbose_name_plural = "Teams"

    team_name = models.CharField(max_length=254, null=True, blank=True)
    team_description = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    team_members = models.ManyToManyField("Team_Members")

    def __str__(self):
        return self.team_name