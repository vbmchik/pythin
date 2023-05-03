from django import forms 
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
class CartAddProductsForm(forms.Form ):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    def __init__(self, *args, **kwargs):
        if 'pquant' in kwargs.keys():
            pquant = kwargs.pop('pquant')
        else:
            pquant = 1
        super(CartAddProductsForm, self).__init__(*args, **kwargs)
        if pquant >1 and pquant < 21:
            self.fields["quantity"].choices = [
            (i, str(i)) for i in range(1, pquant)]
            
        
    

#[x for x in range(9)]