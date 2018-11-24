from rest_framework.serializers import CharField

from dynamic_rest.fields import (
    CountField,
    DynamicField,
    DynamicGenericRelationField,
    DynamicMethodField,
    DynamicRelationField,
)

from dynamic_rest.serializers import DynamicModelSerializer

from vsquare.models import (
    Organization,
    Game,
    Item,
    Difficulty,
    Category,
)

class OrganizationSerializer(DynamicModelSerializer):

    class Meta:
        model = Organization
        name = 'organization'
        fields = (
            'id',
            'url',
            'name'
        )


class GameSerializer(DynamicModelSerializer):

    class Meta:
        model = Game
        name = 'game'
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


class ItemSerializer(DynamicModelSerializer):

    class Meta:
        model = Item
        name = 'item'
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


class DifficultySerializer(DynamicModelSerializer):

    class Meta:
        model = Difficulty
        name = 'difficulty'
        fields = (
            'id',
            'url',
            'name',
            'description',
            'hex'
        )


class CategorySerializer(DynamicModelSerializer):

    class Meta:
        model = Category
        name = 'category'
        fields = (
            'id',
            'url',
            'name',
            'image'
        )
