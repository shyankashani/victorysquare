from vsquare.models import Organization
from rest_framework import serializers

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ('url', 'name')
