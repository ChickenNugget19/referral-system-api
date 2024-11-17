import requests

# Replace with your Django API's base URL
BASE_URL = "http://127.0.0.1:8000/api/users/register/"

# Define the data for registration (example data)
data = {
    "email": "newuser@example.com",
    "name": "Jane Doe",
    "mobile_number": "9876543210",
    "city": "Los Angeles",
    "password": "securepass456"
}

# Send a POST request to register the user
response = requests.post(BASE_URL, data=data)

# Print the response from the API
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
