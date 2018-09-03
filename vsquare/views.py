# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from vsquare.models import Organization, Game, Item, Difficulty, Category
from vsquare.serializers import OrganizationSerializer, GameSerializer, ItemSerializer, DifficultySerializer, CategorySerializer
from rest_framework import viewsets


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DifficultyViewSet(viewsets.ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
