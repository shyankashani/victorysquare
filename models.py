# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Colors(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    hex = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'colors'


class Games(models.Model):
    bgg_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    year_published = models.IntegerField(blank=True, null=True)
    min_players = models.IntegerField(blank=True, null=True)
    max_players = models.IntegerField(blank=True, null=True)
    playing_time = models.IntegerField(blank=True, null=True)
    min_play_time = models.IntegerField(blank=True, null=True)
    max_play_time = models.IntegerField(blank=True, null=True)
    min_age = models.IntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    bgg_average_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bgg_average_rating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class Inventory(models.Model):
    game = models.ForeignKey(Games, models.DO_NOTHING)
    organization = models.ForeignKey('Organizations', models.DO_NOTHING)
    location = models.CharField(max_length=3, blank=True, null=True)
    color = models.ForeignKey(Colors, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    staff_pick = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'inventory'


class KnexMigrations(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    batch = models.IntegerField(blank=True, null=True)
    migration_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knex_migrations'


class KnexMigrationsLock(models.Model):
    is_locked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knex_migrations_lock'


class Organizations(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'organizations'
