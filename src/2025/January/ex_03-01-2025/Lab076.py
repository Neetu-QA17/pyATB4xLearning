# MULTI Level Inheritance

class GrandFather:
    gold = "2kg"

    def home1(self):
        print("1 BHK")


class Father(GrandFather):
    diamond = "22 Karat"

    def home2(self):
        print("2 BHK")


class Son(Father):
    btc = "1Bit Coin"

    def home3(self):
        print("3 BHK")


s = Son()
f = Father
gf = GrandFather()
