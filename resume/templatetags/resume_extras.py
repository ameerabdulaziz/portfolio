from django import template

register = template.Library()


@register.filter
def in_field(items, field):
    return items.filter(field=field)
