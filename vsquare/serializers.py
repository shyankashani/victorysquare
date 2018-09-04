from vsquare.models import Organization, Game, Item, Difficulty, Category
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
        'id',
        'url',
        'name'
    )


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            'id',
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


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'id',
            'url',
            'game',
            'organization',
            'location',
            'difficulty',
            'category',
            'notes',
            'staff_pick'
        )


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = (
            'id',
            'url',
            'name',
            'description',
            'hex'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'url',
            'name',
            'image'
        )
