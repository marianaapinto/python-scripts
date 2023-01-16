#! python3
# password evaluator

import re

def safe_password():

    passwordRegex1 = re.compile (r'\w{8,}')
    passwordRegex2 = re.compile (r'[a-z]{1,}')
    passwordRegex3 = re.compile (r'[A-Z]{1,}')
    passwordRegex4 = re.compile (r'\d+')

#(r'([a-z]){1,}([A-Z]{1,})[0-9]{1,}[._%+-]{1,})')

    password = input('Enter your password: ')
        
    if passwordRegex1.search(password)and passwordRegex2.search(password) and passwordRegex3.search(password) and passwordRegex4.search(password):
        print ('The passord is strong.')
    else:
        print ('Be sure that your passowrd has uppercase, lower case and digit.')
        
        
safe_password()
