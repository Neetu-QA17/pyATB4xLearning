class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel file")

class MySQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from Database")

class TC1:
    def runTC(self):
        ExcelReader().readExcelFile()
        MySQLDBConnection.readMySQLFile()

tc1 = TC1()
tc1.runTC()