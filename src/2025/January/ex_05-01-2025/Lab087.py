from abc import ABC, abstractmethod

class GearBox(ABC):

    @abstractmethod
    def setGear(self):
        pass


class Engine(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        pass

class Car(Engine):

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

    def setGear(self):
        print("Gearbox is ready")

    def drive(self):
        self.start()
        self.setGear()
        self.stop()

car = Car()
car.drive()