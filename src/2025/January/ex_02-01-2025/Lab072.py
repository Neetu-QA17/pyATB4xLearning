# Public
# Private
# Protected

class Myclass:
    public_var = "I am Public"
    __private_var = "I am Private"
    _protected_var = "I am Protected"

object = Myclass()
print(object.public_var)
print(object._protected_var)    # protected is available within the same package
print(object.__private_var)     # private is available only within the class

