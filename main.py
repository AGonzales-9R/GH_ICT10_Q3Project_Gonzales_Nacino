# ICT 10 Skills Test: Account Creation

from pyscript import display, document

def signUP(e):
    document.getElementById("req").innerHTML=" "
    username = document.getElementById("inputUN").value
    password = document.getElementById("inputPass").value
    uservalue = len(username)
    passL = list(password)
    check = [password.isalpha(), password.isdigit()]
    passvalue = len(password)

    if uservalue >= 7:
        if passvalue >= 10:

            if password.isalpha() == True:
                display(f"The password must contain at least one number. Try Again.", target="req")
            
            elif password.isdigit() == True:
                display(f"The password must contain at least one letter. Try Again.", target="req")
            
            elif password.isdigit() == False and password.isalpha() == False:
                display(f"Signing in...", target="req")

        else:
            display(f"The password must contain at least ten characters. Try Again.", target="req")
    
    else:
        display(f"The username must contain at least seven characters. Try Again.", target="req")



