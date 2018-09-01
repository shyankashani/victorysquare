# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    game = models.ForeignKey(Game)
    organization = models.ForeignKey(Organization)
    color = models.ForeignKey(Color)
    category = models.ForeignKey(Category)
    notes = models.CharField()
    location = models.CharField()
    staff_pick = models.BooleanField()

class Game(models.Model):
    bgg_id = models.IntegerField()
    name = models.CharField()
    description = models.CharField()
    year_published = models.IntegerField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    playing_time = models.IntegerField()
    min_playing_time = models.IntegerField()
    max_playing_time = models.IntegerField()
    min_age = models.IntegerField()
    
