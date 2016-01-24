from django.forms.util import flatatt
from django import forms
from django.utils.html import conditional_escape, format_html, html_safe
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.utils.encoding import force_str, force_text, python_2_unicode_compatible


class ReadOnlyWidget(forms.Widget):
    def render(self, name, value, attrs):
        final_attrs = self.build_attrs(attrs, name=name)
        if hasattr(self, 'initial'):
            value = self.initial
        return format_html('<div{}>\r\n{}</div>', flatatt(final_attrs), force_text(value))
        # return "<text{0}".format(flatatt(final_attrs), force_text(value))
    
    def _has_changed(self, initial, data):
        return False

class ReadOnlyField(forms.Field):
    widget = ReadOnlyWidget
    def __init__(self, widget=None, label=None, initial=None, help_text=None):
        super(type(self), self).__init__(self, label=label, initial=initial, 
            help_text=help_text, widget=widget)
        self.widget.initial = initial

    def clean(self, value):
        return self.widget.initial