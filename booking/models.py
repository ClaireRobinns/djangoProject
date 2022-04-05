from django.db import models
from django.core.exceptions import ValidationError
import datetime
from blogs.models import create_id
# Create your models here.

def dateValiator(date):
    events = [booking.eventDate for booking in Book.objects.all() if date == booking.eventDate]
    if date <= datetime.today():
        raise ValidationError('The date cannot be in the past!')
    elif len(events) >= 3:
        raise ValidationError(f'The date of {date} is full access. Try Tomorrow or other days. Thank you.')
    return date


class Book(models.Model):
    id = models.BigAutoField(primary_key=True, default=create_id, editable=False)
    client = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=150, blank=False)
    mobile = models.CharField(max_length=13, blank=False)
    eventDate = models.DateField() # auto_now_add=False,

    def __str__(self):
        return f'{self.client} -> {self.eventDate}'


