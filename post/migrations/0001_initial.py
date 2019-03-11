# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-11 12:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=20)),
                ('image', models.ImageField(max_length=20, upload_to=b'')),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=20)),
                ('image', models.ImageField(max_length=20, upload_to=b'')),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=20)),
                ('image', models.ImageField(max_length=20, upload_to=b'')),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.category')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.category'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.category'),
        ),
    ]
