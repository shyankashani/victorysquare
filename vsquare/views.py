# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from vsquare.models import Organization
from rest_framework import viewsets
from vsquare.serializers import OrganizationSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
