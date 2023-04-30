from django import forms
PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in range(1,21)]

class CartAddProductsForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOISES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget= forms.HiddenInput)
    
    