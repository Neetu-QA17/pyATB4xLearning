# ABSTRACTION
# ABC is a n abstract class which we need to inherit to create an incomplete method

from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Neetu(Father):
    def loan(self):
        print("Loan Completed")

n = Neetu("1Lakh")
n.loan()