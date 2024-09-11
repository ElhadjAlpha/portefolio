from django.contrib import admin
from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(Posts,PostsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'owner', 'created_add')


admin.site.register(Comment,CommentAdmin)
