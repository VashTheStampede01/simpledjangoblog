# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(category)
class newsadmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'body', 'category', 'created_date']
    list_filter = ('title', 'slug', 'image', 'body', 'category', 'created_date')
    search_fields = ['title', 'slug', 'image', 'body', 'category', 'created_date']
    list_per_page = 20
admin.site.register(news, newsadmin)

class blogadmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'body', 'category', 'created_date']
    list_filter = ('title', 'slug', 'image', 'body', 'category', 'created_date')
    search_fields = ['title', 'slug', 'image', 'body', 'category', 'created_date']
    list_per_page = 20
admin.site.register(blog, blogadmin)

class articleadmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'body', 'category', 'created_date']
    list_filter = ('title', 'slug', 'image', 'body', 'category', 'created_date')
    search_fields = ['title', 'slug', 'image', 'body', 'category', 'created_date']
    list_per_page = 20
admin.site.register(article, articleadmin)