# reverse inheritance is not possible

class Parent:
    gold = "2kg"

    def flat1(self):
        print("2BHK")

class Child(Parent):

    def flat2(self):
        print("3BHK")

child_obj = Child()
print(child_obj.gold)
child_obj.flat2()

father_obj = Parent()
father_obj.flat1()
father_obj.flat2()   # not possible 'Parent' object has no attribute 'flat2'