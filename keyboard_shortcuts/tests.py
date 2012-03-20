from django import template
from keyboard_shortcuts import settings as ks_settings
from django.test import TestCase
from keyboard_shortcuts.utils import get_processed_hotkeys
from keyboard_shortcuts.utils import get_key_codes
from keyboard_shortcuts.utils import get_combination_action


class TemplateTagTest(TestCase):

    def setUp(self):
        self.template = '{% load hotkeys %}{% setup_hotkeys %}'
        self.original_hotkeys = getattr(ks_settings, 'HOTKEYS')
        ks_settings.HOTKEYS = list()
        ks_settings.HOTKEYS.append({'keys': 'f', 'link': '/test/'})
        ks_settings.SPECIAL_DISABLED = True

    def tearDown(self):
        ks_settings.HOTKEYS = self.original_hotkeys

    def test_valid_hotkeys(self):
        t = template.Template(self.template)
        c = template.Context()
        s = t.render(c)
        self.assertIn(u"var hotkeys = {70: {'link': '/test/'}};", s)
        #  twice the same combination, we consider the last one
        ks_settings.HOTKEYS.append({'keys': 'f', 'link': '/test2/'})
        s = t.render(c)
        self.assertIn(u"var hotkeys = {70: {'link': '/test2/'}};", s)
        ks_settings.HOTKEYS.append({'keys': 'n', 'link': '/next/'})
        s = t.render(c)
        self.assertIn(u"var hotkeys = {78: {'link': '/next/'}, 70: {'link': '/test2/'}};", s)
        # more actions for one combination
        ks_settings.HOTKEYS = [{'keys': 'j', 'js': 'alert(\'J pressed\');', 'link': '/test/'}]
        s = t.render(c)
        self.assertIn(u"var hotkeys = {74: {'link': '/test/'}};", s)

    def test_hotkey_to_js(self):
        ks_settings.HOTKEYS = [{'keys': 'j', 'js': 'alert(\'J pressed\');'}]
        t = template.Template(self.template)
        c = template.Context()
        s = t.render(c)
        self.assertIn(u"var hotkeys = {74: {\'js\': \"alert(\'J pressed\');\"", s)
        ks_settings.HOTKEYS = [{'keys': 'j', 'js': '$(\'#elem\').hide();'}]
        s = t.render(c)
        self.assertIn(u"var hotkeys = {74: {\'js\': \"$('#elem').hide();\"", s)

    def test_invalid_hotkeys(self):
        ks_settings.HOTKEYS = list()
        ks_settings.HOTKEYS.append({'keys': '#invalid#', 'link': '/test/'})
        t = template.Template(self.template)
        c = template.Context()
        s = t.render(c)
        self.assertIn(u"var hotkeys = {};", s)

    def test_special_disabled(self):
        ks_settings.SPECIAL_DISABLED = True
        t = template.Template(self.template)
        c = template.Context()
        s = t.render(c)
        self.assertIn(u"var special_disabled = true;", s)
        ks_settings.SPECIAL_DISABLED = False
        s = t.render(c)
        self.assertIn(u"var special_disabled = false;", s)


class UtilsTest(TestCase):

    def setUp(self):
        self.original_hotkeys = getattr(ks_settings, 'HOTKEYS')
        ks_settings.HOTKEYS = list()
        ks_settings.HOTKEYS.append({'keys': 'f', 'link': '/test/'})

    def tearDown(self):
        ks_settings.HOTKEYS = self.original_hotkeys

    def test_get_processed_hotkeys(self):
        hotkeys = get_processed_hotkeys([{'keys': 'f', 'link': '/test/'}])
        self.assertEquals(hotkeys, {70: {'link': '/test/'}})
        hotkeys = get_processed_hotkeys([{'keys': 'ctrl+f', 'link': '/test/'}])
        self.assertEquals(hotkeys, {17: {70: {'link': '/test/'}}})
        hotkeys = get_processed_hotkeys([{'keys': 'ctrl+alt+f', 'link': '/test/'}])
        self.assertEquals(hotkeys, {17: {18: {70: {'link': '/test/'}}}})
        hotkeys = get_processed_hotkeys([{'keys': 'ctrl+alt+f', 'link': '/test/'},
                                        {'keys': 'ctrl+alt+d', 'link': '/test2/'}])
        self.assertEquals(hotkeys, {17: {18: {68: {'link': '/test2/'}, 70: {'link': '/test/'}}}})
        hotkeys = get_processed_hotkeys([{'keys': 'ctrl+alt+shift+f', 'link': '/test/'}])
        self.assertEquals(hotkeys, {})  # only three levels for now

    def test_get_processed_hotkeys_from_ks_settings(self):
        hotkeys = get_processed_hotkeys([{'keys': 'f', 'link': '/test/'}])
        hotkeys_from_ks_settings = get_processed_hotkeys()
        self.assertEquals(hotkeys, hotkeys_from_ks_settings)

    def test_get_processed_hotkeys_no_hotkeys(self):
        ks_settings.HOTKEYS = None
        hotkeys = get_processed_hotkeys()
        self.assertEquals(hotkeys, dict())

    def test_get_processed_hotkeys_wrong_hotkeys(self):
        ks_settings.HOTKEYS = None
        hotkeys = get_processed_hotkeys([{'keys': 'af', 'link': '/test/'}])
        self.assertEquals(hotkeys, dict())
        hotkeys = get_processed_hotkeys([{'keys': '(', 'link': '/test/'}])
        self.assertEquals(hotkeys, dict())

    def test_valid_get_key_codes(self):
        codes = get_key_codes('F')
        self.assertEquals(codes, [70, ])
        codes = get_key_codes('f')
        self.assertEquals(codes, [70, ])
        codes = get_key_codes('/')
        self.assertEquals(codes, [111, ])
        codes = get_key_codes('backslash \\')
        self.assertEquals(codes, [220, ])
        codes = get_key_codes('meTA')
        self.assertEquals(codes, [224, ])
        codes = get_key_codes('X')
        self.assertEquals(codes, [88, ])
        codes = get_key_codes('X ')
        self.assertEquals(codes, [88, ])
        codes = get_key_codes(' X ')
        self.assertEquals(codes, [88, ])
        codes = get_key_codes(' X')
        self.assertEquals(codes, [88, ])
        codes = get_key_codes('g+h')
        self.assertEquals(codes, [71, 72, ])
        codes = get_key_codes('CTRL + X')
        self.assertEquals(codes, [17, 88, ])
        codes = get_key_codes('CTRL+X')
        self.assertEquals(codes, [17, 88, ])
        codes = get_key_codes(' CTRL + X ')
        self.assertEquals(codes, [17, 88, ])
        codes = get_key_codes('ctrl + x')
        self.assertEquals(codes, [17, 88, ])
        codes = get_key_codes('CTRL +X')
        self.assertEquals(codes, [17, 88, ])
        codes = get_key_codes('CTRL+ALT+X')
        self.assertEquals(codes, [17, 18, 88, ])

    def test_invalid_get_key_codes(self):
        codes = get_key_codes(' ')
        self.assertEquals(codes, [])
        codes = get_key_codes('.a')
        self.assertEquals(codes, [])
        codes = get_key_codes('af')
        self.assertEquals(codes, [])
        codes = get_key_codes('CTRL X')
        self.assertEquals(codes, [])

    def test_get_combination_action(self):
        action = get_combination_action({'keys': 'a'})
        self.assertEquals(action, {})
        action = get_combination_action({'keys': 'a', 'not_valid': 'func();'})
        self.assertEquals(action, {})
        action = get_combination_action({'keys': 'a', 'link': '/test/'})
        self.assertEquals(action, {'link': '/test/'})
        action = get_combination_action({'keys': 'a', 'js': 'func();'})
        self.assertEquals(action, {'js': 'func();'})
