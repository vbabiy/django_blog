from django_blog.blog.models import Post, Category, Tag
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext