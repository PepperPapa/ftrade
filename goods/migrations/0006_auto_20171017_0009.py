# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20171015_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='carouselIMG',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detailIMG1',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detailIMG10',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detailIMG2',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detailIMG3',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detailIMG4',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detailIMG5',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detailIMG6',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detailIMG7',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detailIMG8',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='detailIMG9',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='thumbnail2',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='thumbnail3',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='thumbnail4',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='thumbnail5',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
    ]