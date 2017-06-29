from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Tag


# 让admin post显示更加详细的信息
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


# 注册models
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
