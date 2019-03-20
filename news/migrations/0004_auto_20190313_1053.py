# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-13 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190312_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Article', models.CharField(max_length=2000)),
                ('Arbum_title', models.CharField(max_length=2000)),
                ('log', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='SOME STRING', upload_to='articles/'),
        ),
    ]
