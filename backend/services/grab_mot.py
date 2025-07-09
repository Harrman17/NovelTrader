import requests
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL, SCOPE, API_KEY

def get_bearer_token():
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": SCOPE
    }
    response = requests.post(TOKEN_URL, data=payload)
    response.raise_for_status()
    return response.json()["access_token"]

def get_mot_data(registration):
    token = get_bearer_token()
    formatted_reg = registration.upper().replace(" ", "%20")
    url = f"https://history.mot.api.gov.uk/v1/trade/vehicles/registration/{formatted_reg}"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-API-Key": API_KEY,
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
