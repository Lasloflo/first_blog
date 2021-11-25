from django.contrib import admin

from .models import Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('author',)
    search_fields = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'create_at', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('author', 'post')
    list_filter = ('author', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
