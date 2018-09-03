from vsquare.models import Organization, Game, Item, Difficulty, Category
from rest_framework import serializers


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = (
        'url',
        'name'
    )


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = (
            'url',
            'name',
            'bgg_id',
            'description',
            'year_published',
            'min_players',
            'max_players',
            'playing_time',
            'min_play_time',
            'max_play_time',
            'min_age',
            'thumbnail',
            'image',
            'bgg_average_weight',
            'bgg_average_rating'
        )


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = (
            'url',
            'game',
            'organization',
            'location',
            'difficulty',
            'category',
            'notes',
            'staff_pick'
        )


class DifficultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Difficulty
        fields = (
            'url',
            'name',
            'description',
            'hex'
        )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'url',
            'name',
            'image'
        )
