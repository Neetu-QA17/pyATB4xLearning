# Static Method - can be called directly without creating an object
# static doesn't belong to object - it belongs to class - that the reason, self keyword is not used

class MathOperations:
    def div(self, a, b):
        return a/b

    @staticmethod
    def sum(a, b):
        return a+b


obj = MathOperations()
output1 = obj.div(10, 5)
print(output1)
print(MathOperations.sum(4, 5))