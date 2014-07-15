from django.contrib import admin
from blog.models import Post, Author, Tag, User, Comment
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('name',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('twitter',)
        }),
    )
    list_display = ('name', 'twitter')
    list_filter = ('name', 'twitter')

admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {
            'fields': ('title', 'pub_date', )
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('author', 'body',)
        }),
    )
    list_display = ('title', 'pub_date', 'author', 'body')
    list_filter = ('pub_date', 'author')

admin.site.register(Post, PostAdmin)


admin.site.register(Tag)



admin.site.register(User)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'user', 'comment')

admin.site.register(Comment, CommentAdmin)