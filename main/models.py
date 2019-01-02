from django.db import models
from uuid import uuid4
# Create your models here.
from _datetime import datetime
import os

class Gallery(models.Model):
    name = models.CharField(max_length=120)
    image_thubnail = models.ImageField(upload_to="gallery/thubnail/" + datetime.now().isoformat() + "/")
    image_fullsize = models.ImageField(upload_to='gallery/full_size/' + datetime.now().isoformat() + "/")
    uploaded = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="clients/thubnail/"+ datetime.now().isoformat() + "/")
    uploaded = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    img_thumnail = models.ImageField(upload_to='certificate/images/' + datetime.now().isoformat() + "/")
    file = models.FileField(upload_to='certificate/' + datetime.now().isoformat() + "/")
    uploaded = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        return extension



