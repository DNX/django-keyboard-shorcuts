from keyboard_shortcuts import settings as ks_settings


class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value


def get_combination_action(combination):
    """
    Prepares the action for a keyboard combination, also filters another
    "strange" actions declared by the user.
    """
    accepted_actions = ('link', 'js')
    for action in accepted_actions:
        if action in combination:
            return {action: combination[action]}
    return {}


def get_processed_hotkeys(hotkeys=None):
    """
    Process passed dict with key combinations or the HOTKEYS dict from
    settings.
    """
    hotkeys = hotkeys or ks_settings.HOTKEYS
    processed_hotkeys = AutoVivification()
    if not hotkeys:
        return processed_hotkeys

    for combination in hotkeys:
        key_codes = get_key_codes(combination['keys'])
        if len(key_codes) == 1:
            processed_hotkeys[key_codes[0]] = get_combination_action(combination)
        elif len(key_codes) == 2:
            processed_hotkeys[key_codes[0]][key_codes[1]] = get_combination_action(combination)
        elif len(key_codes) == 3:
            processed_hotkeys[key_codes[0]][key_codes[1]][key_codes[2]] = get_combination_action(combination)
        # TODO: make dynamic vivification

    return processed_hotkeys


def get_key_codes(keys):
    """
    Calculates the list of key codes from a string with key combinations.
    Ex: 'CTRL+A' will produce the output (17, 65)
    """
    keys = keys.strip().upper().split('+')
    codes = list()
    for key in keys:
        code = ks_settings.KEY_CODES.get(key.strip())
        if code:
            codes.append(code)
    return codes
