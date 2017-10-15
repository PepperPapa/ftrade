# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20171013_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='carouselIMG',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='goods',
            name='detailIMG1',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='detailIMG10',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='detailIMG2',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='detailIMG3',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='detailIMG4',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='detailIMG5',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='detailIMG6',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='detailIMG7',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='detailIMG8',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='detailIMG9',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='recommended',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='goods',
            name='thumbnail1',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='thumbnail2',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='thumbnail3',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='thumbnail4',
            field=models.CharField(default='', max_length=800),
        ),
        migrations.AddField(
            model_name='goods',
            name='thumbnail5',
            field=models.CharField(default='', max_length=800),
        ),
    ]