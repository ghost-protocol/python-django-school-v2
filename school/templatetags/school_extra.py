







from django import template
register = template.Library()


@register.filter()
def boldcoffee(value):
    '''Returns input wrapped in HTML  tags'''
    return '%s' % value