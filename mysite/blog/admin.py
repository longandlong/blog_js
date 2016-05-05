from django.contrib import admin

from . models import Article, Comment, Photo, Blog
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(Blog)
# Register your models here.
