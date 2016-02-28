from django import forms
from . import models

class NewMarketingEmailForm(forms.ModelForm):
    class Meta:
        model = models.MarketingEmail
        exclude = ['date']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(NewMarketingEmailForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['user'].queryset = models.User.objects.filter(id=user.id)
            self.fields['user'].initial = models.User.objects.get(id=user.id)
      