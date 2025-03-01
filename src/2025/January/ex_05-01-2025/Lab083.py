# Method Overriding
# Method name is same in parent and child
# Child method always override the parent function
# super keyword - means call my parent function

class GrandFather:

    x= 25
    def home(self):
        print("Old House")

class Father(GrandFather):

    a= 10
    def home(self):
        print("1 Bunglow")
        print(self.a)
        super().home()
        print(super().x)

class Daughter(Father):
    b=20

    def home(self):
        super().home()
        print(super().a)
        print("No house")
        print(self.b)



neetu = Daughter()
neetu.home()   # calling function

#papa = Father()
#papa.home()
# if want to call the function from the Father's class then add super keyword in the child class as above
# use super to access the attribute defined in parent class
# use self to access the attribute defined in the child class
# child can't directly access the grandparent attribute or function