from django import template

register = template.Library()

#for average rating in products
@register.filter
def int_range(value):
    return range(int(value))
