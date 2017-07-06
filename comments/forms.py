from django import forms
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']


class NameForm(forms.Form):
    your_name = forms.CharField(label='light', max_length=100)


# class MyCustomForm(forms.Form):
#     """django_markdown form"""
#     content = forms.CharField(widget=MarkdownWidget())
#     content2 = MarkdownFormField()
