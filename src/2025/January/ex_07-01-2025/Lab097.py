# Exception in a class

class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number\n"))
        except Exception as e:
            print("Enter only value for a")
        else:
            print(a)
        finally:
            print("FINALLY: Anyhow I will be printed")

x = XYZ()
x.f1()
