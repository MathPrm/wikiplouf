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
    # On imbrique les serializers pour avoir les noms au lieu des simples IDs
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = MarineAnimal
        # Les 7 champs minimum demandés par la consigne sont bien présents
        fields = [
            'id', 
            'name', 
            'description', 
            'height', 
            'species', 
            'thumb', 
            'cover', 
            'category', 
            'tags'
        ]