from django import forms
from .models import Book
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import Book
import datetime
from crispy_forms.helper import FormHelper

def dateValidator(date):
    events = [booking.eventDate for booking in Book.objects.all() if date == booking.eventDate]
    if date <= datetime.date.today():
        raise ValidationError('The date cannot be in the past!')
    elif len(events) >= 3:
        raise ValidationError(f'The Date of {events[0]} is full access. Try Tomorrow.')
    return date

# DOY = [int(str(datetime.date.today()).split('-')[0])+i for i in range(5)]

class BookForm(forms.Form):
    client = forms.CharField(max_length=100, label='Name', required=True)
    email  = forms.EmailField(max_length=150, required=True)
    # phoneRegex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    mobile = forms.CharField(required=True, max_length=13)
    eventDate = forms.DateField(required=True, widget=forms.SelectDateWidget(years=[int(str(datetime.date.today()).split('-')[0])+i for i in range(5)]))
    class Meta:
        model = Book
        fields = '__all__'