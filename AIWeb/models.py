from django.db import models
from django import forms
from captcha.fields import CaptchaField
from cloudinary.models import CloudinaryField


class Project(models.Model):
    projectTemplate = CloudinaryField('image')
    projectTitle = models.CharField(default="Title ", max_length=25)
    desc = models.TextField(default="not mentioned")
    projectLink = models.URLField(max_length=200, default="not mentioned")
    created_at = models.DateTimeField(auto_now_add=True)


class contactForm(forms.Form):
    captcha = CaptchaField()


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30, default="not mentioned")
    email = models.EmailField(default="not mentioned")
    phone = models.CharField(max_length=15, default="not mentioned")
    desc = models.TextField(default="not mentioned")

    def __str__(self):
        return f'{self.name} - {self.desc[:15]} ..'


class DigitalNote(models.Model):
    subjectName = models.CharField(max_length=50)
    books = models.JSONField(default=dict)

    def __str__(self):
        return self.subjectName
