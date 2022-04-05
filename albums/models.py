from django.db import models
import os
import datetime


class Categorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Software(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class modelClient(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.name}'


class Album(models.Model):
    name = models.CharField(max_length=50)
    modelName = models.OneToOneField(modelClient, on_delete=models.CASCADE) # I should change OneToOneField --> ForeignKey
    caption = models.CharField(max_length=160, blank=True)
    category = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    softEditor = models.ManyToManyField(Software, blank=True, related_name='software')
    photos = models.ImageField(upload_to=f'media/albums/{modelName}')

    def get_upload_to(self, instance, filename):
        return os.path.join(f'{instance.modelName.name}',f'{instance.slug}', filename)

    def __str__(self):
        return f'{self.name} - {self.category}'

