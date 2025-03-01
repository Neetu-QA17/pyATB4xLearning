# Create Booking Testcase
# Verify that Booking ID is not null, status code, key is always string, etc


import pytest
import allure
import requests

# POSITIVE Test Case
@allure.title("Test GET Request - RestFUL Booker Request")
@allure.description("TC#1 -> Verify that GET request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Neetu Singh")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 200

# NEGATIVE Test Case
@allure.title("Test GET Request - RestFUL Booker Request")
@allure.description("TC#2 -> Verify that GET request with invalid bookingID")
@allure.testcase("TC#2")
@pytest.mark.smoke
def test_get_single_request_by_negative_id():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    assert response_data.status_code == 404

# NEGATIVE Test Case
@allure.title("Test GET Request - RestFUL Booker Request")
@allure.description("TC#3 -> Verify that GET request bookingID containing invalid")
@allure.testcase("TC#3")
@pytest.mark.smoke
def test_get_single_request_by_invalid_id():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    assert response_data.status_code == 404
