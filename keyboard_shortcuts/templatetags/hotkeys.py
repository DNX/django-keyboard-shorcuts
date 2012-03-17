from django.template import Library
from keyboard_shortcuts.utils import get_processed_hotkeys

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
        'hotkeys': get_processed_hotkeys(),
    }
