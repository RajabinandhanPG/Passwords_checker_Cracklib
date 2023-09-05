import cracklib
import string
import re
from colorama import*


def check_password_strength(password):
    try:
        

        strength = True
        
        if len(password) < 8:
             print(Fore.RED+"Password is too short. It should be 8 characters or longer.")
             strength = False
        if not re.search(r'[A-Z]', password):
            print(Fore.RED+"Password must contain at least one uppercase letter.")
            strength = False
        if not re.search(r'[a-z]', password):
            print(Fore.RED+"Password must contain at least one lowercase letter.")
            strength = False
        if not re.search(r'\d', password):
            print(Fore.RED+"Password must contain at least one number.")
            strength = False

        sym_check = False
        for i in  set(string.punctuation):
            if i in password:
                sym_check = True

        if not sym_check:
            print(Fore.RED+"Password must contain at least one symbol.")
            strength = False


        cracklib.FascistCheck(password)

        return strength

    except Exception as e:
        print(Fore.RED+ str(e))
        return False
        

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    pass_check = check_password_strength(password)

    if pass_check:
        print(Fore.GREEN+ "Password is strong.")
    else:
        print(Fore.RED+ "Password is weak. ")