class Calc:

    def sum(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b

obj_ref = Calc()

a = int(input("Enter the value of a\n"))
b = int(input("Enter the value of b\n"))
# setting the objects separately
res_sum = obj_ref.sum(a,b)
res_sub = obj_ref.sub(a,b)
res_mul = obj_ref.mul(a,b)
res_div = obj_ref.div(a,b)

print(res_sum, res_sub, res_mul, res_div)