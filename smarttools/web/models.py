from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    rol = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Competition(models.Model):
    name = models.CharField(max_length=200, null=False)
    image = models.CharField(max_length=200, null=False)
    url = models.CharField(max_length=200, null=False)
    startingDate = models.DateTimeField(null=False)
    deadline = models.DateTimeField(null=False)
    description = models.CharField(max_length=200, null=False)
    user = models.ForeignKey(User, null=False)

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=30, null=False)
    user_email = models.CharField(max_length=30, null=False)
    uploadDate = models.DateTimeField(null=True)
    message = models.CharField(max_length=200, null=False)
    competition = models.ForeignKey(Competition, null=False)
    original_video = models.FileField(upload_to='videos', null=True)
    converted_video = models.FileField(upload_to='videos', blank=True, null=True)

    def __str__(self):
        return self.name

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'user_email', 'message','original_video']
