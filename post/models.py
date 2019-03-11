# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class category(models.Model):
    name = models.CharField(max_length = 20)
    desc = models.TextField()
    def __unicode__(self):
        return self.name

class blog(models.Model):
    title = models.CharField(max_length = 20)
    slug = models.SlugField(max_length = 20)
    image = models.ImageField(max_length = 20, upload_to = 'image')
    body = models.TextField()
    category = models.ForeignKey(category)
    created_date = models.DateTimeField(default = timezone.now)
    publish_date = models.DateTimeField(blank = True, null = True)
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    def __unicode__(self):
        return self.title

class article(models.Model):
    title = models.CharField(max_length = 20)
    slug = models.SlugField(max_length = 20)
    image = models.ImageField(max_length = 20, upload_to = 'image')
    body = models.TextField()
    category = models.ForeignKey(category)
    created_date = models.DateTimeField(default = timezone.now)
    publish_date = models.DateTimeField(blank = True, null = True)
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    def __unicode__(self):
        return self.title

class news(models.Model):
    title = models.CharField(max_length = 20)
    slug = models.SlugField(max_length = 20)
    image = models.ImageField(max_length = 20, upload_to = 'image')
    body = models.TextField()
    category = models.ForeignKey(category)
    created_date = models.DateTimeField(default = timezone.now)
    publish_date = models.DateTimeField(blank = True, null = True)
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    def __unicode__(self):
        return self.title