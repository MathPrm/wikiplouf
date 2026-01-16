from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class MarineAnimal(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    height = models.FloatField(help_text="Taille en mètres")
    species = models.CharField(max_length=255)
    thumb = models.ImageField(upload_to='medias/%Y/%m', blank=True)
    cover = models.ImageField(upload_to='medias/%Y/%m', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name