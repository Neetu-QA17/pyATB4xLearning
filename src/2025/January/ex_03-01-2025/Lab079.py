# HIERARCHIAL INHERITANCE

class Father:
    def home1(self):
        print("2 Bunglow")

class Neetu(Father):
    def home2(self):
        print("3 BHK")

class Anand(Father):
    def home3(self):
        print("1 Bunglow")

class Neelam(Father):
    def no_house(self):
        print("No house")

n = Neetu()
n.home1()
n.home2()

a = Anand()
a.home3()
a.home1()

ne = Neelam()
ne.home1()
ne.no_house()
