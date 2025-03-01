# Match Statements - also known as switch statements in JAVA

#SYNTAX

#  match variable:
#    case pattern1:
#      # code block
#    case pattern2:
#      # code block

# WAP to ask the user - on which browser he wants to run the automation program
browser_name = input("Enter the name of the browser: ")
browser_name = browser_name.lower()  # lower function is used so that
# even if browser name is given in capital letters then also it will match

match browser_name:
    case "edge":
        print("Execute Edge code")
    case "chrome":
        print("Execute Chrome code")
    case "firefox":
        print("Execute Firefox code")
    case "safari":
        print("Execute Safari code")
    case _:
        print("No browser found")