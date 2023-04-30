from django import forms 
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
class CartAddProductsForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    
#[x for x in range(9)]