from django.db import models

# Create your models here.
from django.utils.six import python_2_unicode_compatible
from django_markdown.models import MarkdownField


@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    def __str__(self):
        return self.text[:20]


# class MyModel(models.Model):
#     """django_markdown: M"""
#     content = MarkdownField()
