from django.template import Library
from keyboard_shortcuts.utils import get_processed_hotkeys
from keyboard_shortcuts import settings as ks_settings

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
        'special_disabled': ks_settings.SPECIAL_DISABLED,
    }
