from abc import ABC, abstractmethod


class ExcelReader(ABC):

    @abstractmethod
    def readFromExcel(self):
        pass


class Browser(ExcelReader):

    @abstractmethod
    def start_Browser(self):
        pass

    def stop_Browser(self):
        pass


class TC1(Browser):

    
    def start_Browser(self):
        print("Browser Started")

    def stop_Browser(self):
        print("Browser Stopped")

    def readFromExcel(self):
        print("Data extracted from Excel")

    def runTC(self):
        self.start_Browser()
        self.readFromExcel()
        self.stop_Browser()


tc = TC1()
tc.runTC()
