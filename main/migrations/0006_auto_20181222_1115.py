# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-22 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181222_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='img_thumnail',
            field=models.ImageField(default='test', upload_to='certificate/images/2018-12-22T11:14:51.778916/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certificate',
            name='file',
            field=models.FileField(upload_to='certificate/2018-12-22T11:14:51.778949/'),
        ),
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(upload_to='clients/thubnail/2018-12-22T11:14:51.778163/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image_fullsize',
            field=models.ImageField(upload_to='gallery/full_size/2018-12-22T11:14:51.777393/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image_thubnail',
            field=models.ImageField(upload_to='gallery/thubnail/2018-12-22T11:14:51.777339/'),
        ),
    ]
