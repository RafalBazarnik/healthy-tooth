from django import forms
from . import models

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = models.Purchase
        exclude = ['status', 'total_price', 'purchase_id']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PurchaseForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['purchaser'].queryset = models.User.objects.filter(id=user.id)
            self.fields['purchaser'].initial = models.User.objects.get(id=user.id)
            

class PurchaseStatusChangeForm(forms.ModelForm):
	class Meta:
		model = models.Purchase
		fields = ['status']
		