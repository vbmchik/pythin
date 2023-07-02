class Account:
    
    def __init__(self, iban) -> None:
        self.iban = iban
    
    @staticmethod
    def validate(iban):
        return len(iban) == 20
    
account_numbers = ['8'*20, '44444', '44444444']

for element in account_numbers:
    if Account.validate(element):
        print(f'We can use {element}')
    else:
        print(f'This is wrong! {element}')