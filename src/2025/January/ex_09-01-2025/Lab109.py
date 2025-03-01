from BrowserPackage.OpenBrowser import StartBrowser
from BrowserPackage.CloseBrowser import CloseBrowser

def test_case1():
    StartBrowser()
    print("I am executing the code TC1")
    CloseBrowser()

test_case1()