from django import template

from blog.models import Post, Category

"""
在html中使用{% load blog_tags %} 导入模板标签
"""

register = template.Library()


@register.simple_tag  # 注册为django模板标签
def get_recent_posts(num=5):
    """获取最新的5篇文章"""
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    """按月降序归档"""
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    """分类类别标签"""
    return Category.objects.all()
