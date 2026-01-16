from rest_framework import serializers
from .models import MarineAnimal, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class MarineAnimalSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name')
    tag_names = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
        source='tags'
    )

    class Meta:
        model = MarineAnimal

        fields = [
            'id', 
            'name', 
            'description', 
            'height', 
            'species', 
            'thumb', 
            'cover', 
            'category', 
            'category_name',
            'tags',
            'tag_names'
        ]