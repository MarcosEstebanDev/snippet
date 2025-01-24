from django import template
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

register = template.Library()

@register.filter(name='pygmentize')
def pygmentize(value, language):
    lexer = get_lexer_by_name(language)
    formatter = HtmlFormatter()
    return highlight(value, lexer, formatter)
