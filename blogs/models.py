import datetime
from django.contrib.auth.models import User
from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.category
class EditSoftware(models.Model):
    Software = models.CharField(blank=False, max_length=80)
    def __str__(self):
        return self.Software
class Albums(models.Model):
    photos = models.ImageField(upload_to='media/photos/', validators=[])
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    caption = models.CharField(max_length=80, blank=True)
    edit_software = models.ManyToManyField(EditSoftware, related_name='software', blank=True)
    lens_type = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.caption} - {self.categories}'

def create_id():
    now = datetime.datetime.now()
    return int(str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second))
class Blogging(models.Model):
    # pip install iframe
    id = models.BigAutoField(primary_key=True, default=create_id, editable=False)
    title = models.CharField(validators=[], max_length=200, blank=False)
    content = models.TextField()
    images = models.ImageField(upload_to='media/myblog/', blank=True)
    video = models.FileField(validators=[], blank=True)
    embed_video_url = EmbedVideoField(verbose_name='Youtube Video', blank=True)
    # embed_video = models.EmbedVideoField( blank= True, verbose_name= 'Youtube Embed Video')
    edit_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.created_date}'
