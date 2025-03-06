# API Request - HTTP Request
from logging import lastResort

import pytest
import allure
import requests

@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("TC#1 -> Verify the Create Booking!")
@pytest.mark.crud
def test_create_booking_tc1():
# to make request
# URL
# Method - POST
# Headers - Content-type = Application/json
# Payload/Data/ Body - Dict/ JSON
# Auth - NA
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "/booking"
    URL = base_url + base_path
    header = {"Content-Type" : "application/json"}
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    response = requests.post(url=URL, headers=header, json=payload)
    assert response.status_code == 200
    response_Data = response.json()


    # response body verification
    bookingid = response_Data["bookingid"]
    assert  bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

# To fetch first name, last name, totalprice, depositpaid
    firstname = response_Data["booking"]["firstname"]
    lastname   = response_Data["booking"]["lastname"]
    totalprice = response_Data["booking"]["totalprice"]
    depositpaid = response_Data["booking"]["depositpaid"]
    checkin = response_Data["booking"]["bookingdates"]["checkin"]
    checkout = response_Data["booking"]["bookingdates"]["checkout"]

# Verify the fetched details
    assert  firstname == "Jim"
    assert  lastname == "Brown"
    assert  totalprice == 111
    assert  depositpaid == False
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"



@allure.title("TC#2 - Create Booking CRUD Negative TC#2")
@allure.description("TC#1 -> Verify when Payload is blank!")
@pytest.mark.crud
def test_create_booking_tc2_blank_payload():
# to make request
# URL
# Method - POST
# Headers - Content-type = Application/json
# Payload/Data/ Body - Dict/ JSON
# Auth - NA
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "/booking"
    URL = base_url + base_path
    header = {"Content-Type" : "application/json"}
    payload = {

    }
    response = requests.post(url=URL, headers=header, json=payload)
    assert response.status_code == 500
    response_Data = response.json()


@allure.title("TC#3 - Create Booking CRUD Negative TC#3")
@allure.description("TC#3 -> Verify value for total price is string")
@pytest.mark.crud
def test_create_booking_tc3_incorrect_totalprice_as_string():

    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "/booking"
    URL = base_url + base_path
    header = {"Content-Type" : "application/json"}
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : "neetu",
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    response = requests.post(url=URL, headers=header, json=payload)
    assert response.status_code == 200
    response_Data = response.json()