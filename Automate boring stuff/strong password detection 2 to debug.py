#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip,re

def safe_password():

    passwordRegex1 = re.compile (r'(\w{8,})([a-z]{1,})([A-Z]{1,})(\d+)')

#(r'([a-z]){1,}([A-Z]{1,})[0-9]{1,}[._%+-]{1,})')

    password = input('Enter your password: ')
    
    
    test = passwordRegex1.search(password)
    
    if test.group(1) and test.group(2) and test.group(3) and test.group(4): 
        print ('The passord is strong.')
    else:
        print ('Be sure that your passowrd has uppercase, lower case and digit.')
    

      
safe_password()
