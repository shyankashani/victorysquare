from __future__ import unicode_literals

from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'organizations'


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'categories'


class Difficulty(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    hex = models.CharField(max_length=7)

    class Meta:
        db_table = 'colors'


class Game(models.Model):
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

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'games'


class Item(models.Model):
    game = models.ForeignKey(Game, models.DO_NOTHING)
    organization = models.ForeignKey('Organization', models.DO_NOTHING)
    location = models.CharField(max_length=3, blank=True, null=True)
    color = models.ForeignKey(Difficulty, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    staff_pick = models.NullBooleanField()

    class Meta:
        db_table = 'inventory'


class KnexMigrations(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    batch = models.IntegerField(blank=True, null=True)
    migration_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'knex_migrations'


class KnexMigrationsLock(models.Model):
    is_locked = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'knex_migrations_lock'
