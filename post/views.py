# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from vanilla import ListView, DetailView
from post.models import *
# Create your views here.
class bloglist(ListView):
    model = blog
class articlelist(ListView):
    model = article
class newslist(ListView):
    model = news
class blogdetail(DetailView):
    model = blog
class articledetail(DetailView):
    model = article
class newsdetail(DetailView):
    model = news