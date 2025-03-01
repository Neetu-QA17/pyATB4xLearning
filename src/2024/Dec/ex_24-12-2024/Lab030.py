# Match Statement - same as switch statement in java
#match variable:
#    case pattern1:
    # code block

#    case pattern2:
    # code block2

# wap to ask the user input that which browser needs to be used for automation
browser_name = input("Enter the browser to be utilized for automation: ")
browser_name = browser_name.upper()
match browser_name:
    case "chrome":
        print("Execute the code in Chrome browser")
    case "edge":
        print("Execute the code in Edge browser")
    case "firefox":
        print("Execute the code in Firefox browser")
    case "safari":
        print("Execute the code in Safari browser")
    case _:
        print("Not Defined, Kindly select the correct browser")