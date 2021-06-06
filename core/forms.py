from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ['user']

	def __init__(self, *args, **kwargs):
		self.field_order = ['title', 'deadline', 'message']
		super(OrderForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'un', 'placeholder': field.title()})
			self.fields['deadline'].widget.attrs.update({'class': 'un datepicker'})