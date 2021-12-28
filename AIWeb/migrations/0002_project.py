# Generated by Django 4.0 on 2021-12-28 17:25

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectTemplate', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('desc', models.TextField(default='not mentioned')),
                ('projectLink', models.URLField(default='not mentioned')),
            ],
        ),
    ]
