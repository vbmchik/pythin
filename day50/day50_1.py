def check_password( password ):
    if len(password) > 9:
        return True
    if len(password)<=6:
        return False
    if(password.lower() == 'password'):
        return False
    digs = [ x for x in password if x.isdigit()]
    letters = set(digs)^set(password)
    return len(digs) and len(letters) and len(set(password)) > 3

print(check_password('PASSWORD12345'))