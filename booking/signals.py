from django.db.models.signals import post_save, pre_save
from .models import Book
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

# @receiver(post_save, sender=Book)
# def send_email(sender, instance, **kwargs):
#     to_email = instance.email
#     from_email = User.email
#     subject1 = 'Booking Complete!!!'
#     subject2 = ''
#     message1 = '''
#     <p> Hi {}, I am so excited to be working with you! Please wait for ...</p>
#     '''.format(instance.client)
#     message2 = ''
#     send_mail(subject1, message1, from_email, to_email, fail_silently=False)


