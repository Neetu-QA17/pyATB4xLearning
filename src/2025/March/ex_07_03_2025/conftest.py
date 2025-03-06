import pytest
import requests


# can keep the re-usable code here

# Create Token - POST request
@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    return token


# Create Booking - Post
@pytest.fixture()
def create_booking_id():
    print("Create Booking Test Case")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Neetu",
        "lastname": "Singh",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 200

    # Get the response Body and verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["booking_id"]
    return booking_id

@pytest.fixture()
def launch_browser():
    print("Browser is Launched!! Chrome")
    return "Chrome"

@pytest.fixture()
def close_browser():
    print("Closing the Browser!! Chrome")
    return "closed"

@pytest.fixture()
def read_url_testdata_excel():
    pass