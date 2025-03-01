import pytest
import allure

@pytest.mark.smoke
def test_verify_sum1():
    assert 1+1 == 2

@pytest.mark.smoke
def test_verify_sum2():
    assert 1+1 == 1

@pytest.mark.reg
def test_verify_sub():
    assert 2-2 == 0

def test_verify_mul():
    assert 2*5 == 10
@pytest.mark.smoke
def test_verify_div():
    assert 10/2 == 5

@pytest.mark.skip(reason = "Not Applicable for now, Skip the same") # reason is optional
def test_verify_sub():
    assert 0-0 != 0