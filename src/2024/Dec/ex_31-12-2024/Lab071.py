# Web Automation - Selenium
# we will be automating the login Page of vwo website

class VWOLoginPage:

    # creating constructor
    def __init__(self, email_arg, password_arg):  # whatever user will pass
        self.email = email_arg
        self.password = password_arg
        # above email and password are the instance variable

    def login_confirm(self):
        if self.email == "neetu.singh@gmail.com" and self.password == "Pass123":
            print("User logged in successfully")
        else:
            print("Incorrect Credential")
# This is the end of the class

email = input("Enter the email\n")
password = input("Enter the password\n")

# creation of object
vwo_obj = VWOLoginPage(email, password)
vwo_obj.login_confirm()
