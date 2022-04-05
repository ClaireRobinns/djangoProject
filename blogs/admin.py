from django.contrib import admin
from .models import Blogging
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models

# Register your models here.
admin.site.register(Blogging)
