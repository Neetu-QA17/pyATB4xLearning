# Environment Variable
# Instead of saving the credential in the framework we will use the concept of Environment Variable
# i.e. dotenv file

from dotenv import load_dotenv
import os

def test_update_req():
    load_dotenv()  # command to load the file
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

# to showcase to user that yes it has picked hte correct data from dotenv file, print the cred
    print(username)
    print(password)