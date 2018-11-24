# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from dynamic_rest.viewsets import DynamicModelViewSet

from vsquare.models import (
    Organization,
    Game,
    Item,
    Difficulty,
    Category
)

from vsquare.serializers import (
    OrganizationSerializer,
    GameSerializer,
    ItemSerializer,
    DifficultySerializer,
    CategorySerializer
)


class OrganizationViewSet(DynamicModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class GameViewSet(DynamicModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class ItemViewSet(DynamicModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DifficultyViewSet(DynamicModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class CategoryViewSet(DynamicModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
