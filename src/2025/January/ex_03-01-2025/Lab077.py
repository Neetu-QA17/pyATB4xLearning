# MULTIPLE INHERITANCE
# Diamond problem - when there is same function name in 2 different classes
# that function from the class will be called first which was mentioned 1st while creating the object of the class


class Father:

    key = "ABC123"
    __password = "private"    # private variable defined

    def __show_password(self):    # private function is defined
        print(self.__password)


    def father_money(self):
        return 5


    def home(self):
        return "This is from Father"

    def show_everything(self):
        self.__show_password()


class Mother:

    def mother_money(self):
        return 2

    def home(self):
        return "This is from Mother"


class Son(Mother, Father):
    pass

class Son2(Father, Mother):
    pass

s1 = Son()
print(s1.father_money())
print(s1.mother_money())
print(s1.home())
print(s1.key)
s1.show_everything()   # when function is called using the object no need to add print statement

print("---------------------")

s2 = Son2()
print(s2.father_money())
print(s2.mother_money())
print(s2.home())
