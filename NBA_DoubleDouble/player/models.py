from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Player(models.Model):
    name      = models.CharField(max_length=25)
    team      = models.CharField(max_length=25,default='')
    opponent_team   = models.CharField(max_length=25,default='')
    team_result     = models.CharField(max_length=25,default='')

    def __unicode__(self):
        return self.name
