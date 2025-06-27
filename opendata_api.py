import requests
import json

# Your API key
api_key = "VED90OpzjW79pwO6Vkt4Q8fpTeIou5ZU8Vm3a40v"

# The API endpoint
url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

# Get the registration number from the user
plate = input("Enter registration plate: ")

# Set the required headers. 'Content-Type' is handled automatically by 'requests'
# when using the 'json' parameter.
headers = {
  'x-api-key': api_key
}

# Create the payload as a Python dictionary.
# This is the modern and correct way to do it.
payload = {
  "registrationNumber": plate
}

# Make the POST request, passing the dictionary to the 'json' parameter
# requests will handle converting it to a JSON string.
try:
    response = requests.post(url, headers=headers, json=payload)
    
    # Raise an exception if the request returned an HTTP error code (like 4xx or 5xx)
    response.raise_for_status() 

    # Print the JSON response in a readable format
    print("--- Success ---")
    # response.json() parses the JSON response into a Python dictionary
    print(json.dumps(response.json(), indent=2))

except requests.exceptions.HTTPError as err:
    print(f"--- HTTP Error ---")
    print(f"Status Code: {err.response.status_code}")
    # Try to print the error response from the API
    print(f"Response: {err.response.text}")
except requests.exceptions.RequestException as e:
    print(f"--- An error occurred ---")
    print(e)