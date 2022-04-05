from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import AdminFileWidget
from .models import Categorie, Album, modelClient, Software


admin.site.register(Categorie)
admin.site.register(modelClient)
admin.site.register(Software)
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField:{
            'widget': AdminFileWidget(attrs={
                'multiple': True,
            })
        }
    }