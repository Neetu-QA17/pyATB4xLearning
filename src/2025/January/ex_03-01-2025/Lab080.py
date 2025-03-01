# HYBRID INHERITANCE
# multiple types of inheritance - single, multiple, multi-level


class A:
    def methodA(self):  # Father
        return "Method A"

class B(A):
    def methodB(self):   # Brother
        return  "Method B"

class C(A):   # My Elder Sister
    def methodC(self):
        return "Method C"

class D(B, C):  # its me
    def methodD(self):
        return "Method D"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())