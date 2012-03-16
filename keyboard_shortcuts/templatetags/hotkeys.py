from django.conf import settings
from django.template import Library

register = Library()


@register.inclusion_tag('keyboard_shortcuts/hotkeys.js.tpl')
def setup_hotkeys():
    """
    DSetup.
    Ex.
        {% load hotkeys %}
        {% setup_hotkeys %}
    """
    return {
        'hotkeys': settings.HOTKEYS,
    }
