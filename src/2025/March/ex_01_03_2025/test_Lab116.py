# How to create a Test Case in Allure?
# Step1: Import pytest
# Step2: Import allure
# Write a test case as def test_sum():
#                          assert 2-2=0
# Also can add a marking as: @pytest.mark.smoke
# can provide title as: @allure.title("TC1: verify the subtraction")
# can provide description as: @allure.title("This is a smoke test case")

import pytest
import allure

@pytest.mark.smoke
def test_verify_sum2():
    assert 1+1 == 1

@pytest.mark.reg
def test_verify_sub():
    assert 2-2 == 0

@pytest.mark.smoke
def test_verify_mul():
    assert 2*5 == 10

@pytest.mark.smoke
def test_verify_div():
    assert 10/2 == 5
