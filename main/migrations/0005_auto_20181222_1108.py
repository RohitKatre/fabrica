# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-22 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20181222_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('file', models.FileField(upload_to='certificate/2018-12-22T11:08:21.647669/')),
                ('uploaded', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(upload_to='clients/thubnail/2018-12-22T11:08:21.647051/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image_fullsize',
            field=models.ImageField(upload_to='gallery/full_size/2018-12-22T11:08:21.646429/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image_thubnail',
            field=models.ImageField(upload_to='gallery/thubnail/2018-12-22T11:08:21.646386/'),
        ),
    ]