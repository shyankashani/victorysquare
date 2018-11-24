from rest_framework.serializers import CharField

from dynamic_rest.fields import (
    CountField,
    DynamicField,
    DynamicGenericRelationField,
    DynamicMethodField,
    DynamicRelationField,
)

from dynamic_rest.serializers import DynamicModelSerializer

from victorysquare.models import (
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
            'name'
        )


class GameSerializer(DynamicModelSerializer):

    class Meta:
        model = Game
        name = 'game'
        fields = (
            'id',
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
    game = DynamicRelationField('GameSerializer', embed=True)
    organization = DynamicRelationField('OrganizationSerializer', embed=True)
    difficulty = DynamicRelationField('DifficultySerializer', embed=True)
    category = DynamicRelationField('CategorySerializer', embed=True)

    class Meta:
        model = Item
        name = 'item'
        fields = (
            'id',
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
            'name',
            'image'
        )
