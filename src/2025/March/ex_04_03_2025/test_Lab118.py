# PUT request
# URL
# Path - Booking ID
# Token - Auth
# Payload
# Headers

import requests
import pytest
import allure


# Create Token - POST request
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
def create_booking():
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


def test_put_request_positive():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking())
    PUT_url = base_url + base_path
    cookie = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
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
    response = requests.put(url=PUT_url, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Neetu"

    def test_delete():
        URL = "https://restful-booker.herokuapp.com/booking/"
        booking_id = create_booking()
        DELETE_url = URL + str(booking_id)
        cookie_value = "token" + create_token()
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie
        }
        print(headers)
        response = requests.delete(url=DELETE_url, headers=headers)