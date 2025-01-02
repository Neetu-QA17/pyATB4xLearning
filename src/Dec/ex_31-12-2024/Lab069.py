class Calc:

    # Parameterized constructor
    # for instance variable we will use self
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a +self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

obj_ref = Calc(10,5)
output = obj_ref.sum()
output = obj_ref.sub()
output = obj_ref.mul()
output = obj_ref.div()
print(output)

