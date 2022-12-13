from django import forms
from .models import *
# Create your forms here.

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		exclude = ()
		feilds = ['subject', 'name', 'email', 'message']
		
	subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))

	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' }))
	message = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control' }))

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ('complete','date_ordered')
		feilds = '__all__'
		
class OrderForm2(forms.ModelForm):
	class Meta:
		model = Order2
		exclude = ('complete','date_ordered')
		feilds = '__all__'
		
