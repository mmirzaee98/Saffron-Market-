from django.contrib import admin
from blog.models import Blog, BlogComment

# register blog models in admin panel
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','author','view','date_create','date_update']
    list_filter = ['author','view','date_create','date_update']
    search_fields = ['title','author']

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['user','text','rate','blog','date']
    list_filter = ['user','rate','blog','date']
    search_fields = ['user','text']

