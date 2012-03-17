import re
from django.conf import settings


def get_processed_hotkeys(hotkeys=None):
    processed_hotkeys = dict()
    hotkeys = hotkeys or getattr(settings, 'HOTKEYS', None)
    if not hotkeys:
        return processed_hotkeys

    for combination in hotkeys:
        key = combination['keys'].upper()
        if re.match(r'^[A-Z]$', key):
            processed_hotkeys[ord(key)] = {'link': combination['link']}

    return processed_hotkeys
