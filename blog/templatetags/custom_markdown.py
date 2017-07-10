from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from markdown import markdown

register = template.Library()


@register.filter(is_safe=True)  # 注册template filter
@stringfilter
def custom_markdown(value):
    return mark_safe(markdown(value,
                              extensions=[
                                  'markdown.extensions.fenced_code',  # 识别代码
                                  'markdown.extensions.codehilite',  # 代码高亮
                                  'markdown.extensions.toc',  # 目录
                                  'markdown.extensions.extra',
                                  'markdown.extensions.admonition',
                                  'markdown.extensions.headerid',
                                  'markdown.extensions.meta',
                                  'markdown.extensions.nl2br',
                                  'markdown.extensions.sane_lists',
                                  'markdown.extensions.smarty',
                                  'markdown.extensions.wikilinks',
                              ],
                              safe_mode=True,
                              enable_attributes=False))
