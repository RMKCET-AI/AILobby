from django.db import models
from django import forms
from captcha.fields import CaptchaField


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
