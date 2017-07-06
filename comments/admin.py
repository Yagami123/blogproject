from django.contrib import admin

# Register your models here.
# from django_markdown.admin import MarkdownModelAdmin

from blog.models import Post
# from comments.models import MyModel

# admin.site.register(MyModel, MarkdownModelAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'title', 'author', 'translator', 'publisher', 'type',)
    list_filter = ('type', 'publisher',)
    search_fields = ('id', 'title', 'isbn',)
    list_per_page = 20


# admin.site.register(Book)
# admin.site.register(Post, MarkdownModelAdmin)
