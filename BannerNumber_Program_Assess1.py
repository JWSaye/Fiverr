"""
This is the front end of the new login system
in which existing members can log in from and
new members can create an account
"""

# User selects to either login with a 1 or register with a 2 in a loop until a valid input is entered
sel = 0
while sel != 1 and sel != 2:
    sel = int(input('''Please enter the number of your selection:
1. Login with existing account
2. Create new account
: '''))
    if sel != 1 and sel != 2:
        print('Please enter a valid input')

# In the case of a login attempt
if sel == 1:
    # Opens the text file storing the login information
    logins = open("Logins.txt", "r")
    # Gets input for the users username
    user = input("Please enter your username: ")
    # Checks each line in the text file storing the login information
    usrchk = False
    for line in logins:
        # Splits the given line into a list for checking input
        ln = line.split(" ")
        # Checks the inputted username with the line that the loop is on
        if user == ln[0]:
            # Conditional to print too many attempts message
            usrchk = True
            paswdchk = False
            # Loops through getting up to three inputs for the password
            for i in range(3):
                # Gets password input from user
                paswd = input("Please enter your password: ")
                # Checks if the inputted password is the valid password for the username inputted
                if paswd == ln[1]:
                    # Sets conditional true if password is correct
                    paswdchk = True
                    # Prints confirmation of login
                    print("Welcome " + user)
                    logins.close()
                    break
                else:
                    # Prints the amount of attempts left
                    print(str((2 - i)) + " attempts left")
                    continue
            # Prints a 3 failed password attempts statement
            if paswdchk:
                break
            if not paswdchk:
                print("Three failed password attempts")
                logins.close()
                break
        else:
            continue
    # Prints if the user inputs an incorrect username
    if not usrchk:
        print("Invalid username")
        logins.close()
# In the case of a sign up
elif sel == 2:
    print("Welcome new user, let's get your account set up")
    # Gets users first name
    fname = input("Please enter your first name: ")
    # Gets users second name
    sname = input("Please enter your surname: ")
    usr = ''
    # Creates username for user based on the first name and surname
    if len(fname) <= 3:
        usr = usr + fname.lower()
    else:
        usr = usr + fname[:3].lower()
    if len(sname) <= 3:
        usr = usr + sname.lower()
    else:
        usr = usr + sname[:3].lower()
    # Instruction for password creation
    print("""Your password must contain all of the following:
One upper case letter
One lower case letter
One Number
One of these special characters (! £ $ % & @ # ?)
At least 8 characters but no more than 16""")
    cond = False
    # Lists for checking for a special character and numbers
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    chars = ["!", "£", "$", "%", "&", "@", "#", "?"]
    # While loop to create a valid password
    while not cond:
        # Gets desired password from user
        pas = input("Please enter your new password: ")
        # Checks all of the required characteristics of the password
        numchk = False
        upchk = False
        lowchk = False
        charchk = False
        lenchk = False
        for i in pas:
            # Checks for a number
            if i in numbers:
                numchk = True
            # Checks for a special character
            if i in chars:
                charchk = True
            # Checks for a lowercase letter
            if i.islower():
                lowchk = True
            # Checks for an upper case letter
            if i.isupper():
                upchk = True
            # Checks the length of the password
            if 8 <= len(pas) <= 16:
                lenchk = True
            cond = numchk and charchk and lowchk and upchk and lenchk
        # Prints message if all the conditions aren't met
        if not cond:
            print("Password does not meet requirements, try again")
    # Opens Logins file
    logins = open("Logins.txt", "a")
    # Writes a new line and the new credentials to the file
    logins.write("\n")
    logins.write(usr + " " + pas)
    # Closes the file
    logins.close()
    # Confirmation message
    print("You have been signed up with the username of " + usr + ".")