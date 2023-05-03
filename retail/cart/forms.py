from django import forms 
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
class CartAddProductsForm(forms.Form ):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    def __init__(self, *args, **kwargs):
        super(CartAddProductsForm, self).__init__()
        if "pquant" in kwargs:
            self.fields["quantity"].choices = [
                (i, str(i)) for i in range(1, int(kwargs["pquant"]))]
        
        
    

#[x for x in range(9)]