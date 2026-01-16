from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from django.contrib import admin
from .models import Category, Tag, MarineAnimal

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(MarineAnimal)
class MarineAnimalAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ('name', 'display_thumb','species', 'height', 'category')
    
    # Filtres sur le côté droit
    list_filter = ('category', 'species')
    
    # Barre de recherche
    search_fields = ('name', 'description')
    
    # Organisation du formulaire d'édition
    fieldsets = (
        ('Informations Générales', {
            'fields': ('name', 'species', 'description', 'height')
        }),
        ('Classification & Tags', {
            'fields': ('category', 'tags')
        }),
        ('Médias', {
            'fields': ('thumb', 'cover')
        }),
    )
    
    def display_thumb(self, obj):
        if obj.thumb:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.thumb.url)
        return None
    
