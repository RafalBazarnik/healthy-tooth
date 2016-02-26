from django import forms
from . import models

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = models.Purchase
        exclude = ['status', 'total_price', 'purchase_id']

class PurchaseStatusChangeForm(forms.ModelForm):
	class Meta:
		model = models.Purchase
		fields = ['status']
		