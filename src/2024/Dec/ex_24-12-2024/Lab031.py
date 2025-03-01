user_type = input("Enter the user type: admin, manager or guest: ")

match user_type:
    case "admin" | "manager":
        print("Hello Sir")
    case "guest":
        print("Hi Sir")
    case _:
        print("Hello There!")