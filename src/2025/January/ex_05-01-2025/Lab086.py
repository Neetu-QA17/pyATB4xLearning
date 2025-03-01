from abc import ABC, abstractmethod

class PyATB(ABC):

    @abstractmethod
    def payFee(self):
        pass

    def enrolled(self):
        print("Enrolled")


class Neetu(PyATB):
    def payFee(self):
        print("Fees Paid")


n = Neetu()
n.enrolled()