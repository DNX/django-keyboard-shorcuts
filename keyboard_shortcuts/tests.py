from django import template
from django.conf import settings
from django.test import TestCase
from keyboard_shortcuts.utils import get_processed_hotkeys


class TemplateTagTest(TestCase):

    def setUp(self):
        self.template = '{% load hotkeys %}{% setup_hotkeys %}'
        self.original_hotkeys = getattr(settings, 'HOTKEYS')
        settings.HOTKEYS = list()
        settings.HOTKEYS.append({'keys': 'f', 'link': '/test/'})

    def tearDown(self):
        settings.HOTKEYS = self.original_hotkeys

    def test_valid_hotkeys(self):
        t = template.Template(self.template)
        c = template.Context()
        s = t.render(c)
        self.assertIn(u"var hotkeys = {70: {'link': '/test/'}};", s)

    def test_invalid_hotkeys(self):
        t = template.Template(self.template)
        c = template.Context()
        s = t.render(c)
        self.assertIn(u"var hotkeys = {70: {'link': '/test/'}};", s)


class UtilsTest(TestCase):

    def setUp(self):
        self.original_hotkeys = getattr(settings, 'HOTKEYS')
        settings.HOTKEYS = list()
        settings.HOTKEYS.append({'keys': 'f', 'link': '/test/'})

    def tearDown(self):
        settings.HOTKEYS = self.original_hotkeys

    def test_get_processed_hotkeys(self):
        hotkeys = get_processed_hotkeys([{'keys': 'f', 'link': '/test/'}])
        self.assertEquals(hotkeys, {70: {'link': '/test/'}})

    def test_get_processed_hotkeys_from_settings(self):
        hotkeys = get_processed_hotkeys([{'keys': 'f', 'link': '/test/'}])
        hotkeys_from_settings = get_processed_hotkeys()
        self.assertEquals(hotkeys, hotkeys_from_settings)

    def test_get_processed_hotkeys_no_hotkeys(self):
        settings.HOTKEYS = None
        hotkeys = get_processed_hotkeys()
        self.assertEquals(hotkeys, dict())
