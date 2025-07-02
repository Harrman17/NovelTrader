import requests
import json

def get_tax_band(co2):
    bands = [
        (0, 100, "A", 20),
        (101, 110, "B", 20),
        (111, 120, "C", 35),
        (121, 130, "D", 165),
        (131, 140, "E", 195),
        (141, 150, "F", 215),
        (151, 165, "G", 265),
        (166, 175, "H", 315),
        (176, 185, "I", 345),
        (186, 200, "J", 395),
        (201, 225, "K", 430),
        (226, 255, "L", 735),
        (256, float("inf"), "M", 760)
    ]

    for low, high, band, price in bands:
        if low <= co2 <= high:
            return {
                "band": band,
                "price": price
            }
    return {
        "band": "Unknown",
        "price": "Unknown"
    }

def data(plate):
    api_key = "VED90OpzjW79pwO6Vkt4Q8fpTeIou5ZU8Vm3a40v"
    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    headers = {'x-api-key': api_key}
    payload = {"registrationNumber": plate}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print("--- Success ---")
    except requests.exceptions.HTTPError as err:
        print("--- HTTP Error ---")
        print(f"Status Code: {err.response.status_code}")
        print(f"Response: {err.response.text}")
        return
    except requests.exceptions.RequestException as e:
        print("--- An error occurred ---")
        print(e)
        return

    vehicle_data = response.json()

    # ✅ Add tax band and price
    co2 = vehicle_data.get("co2Emissions", None)
    if co2 is not None:
        tax_info = get_tax_band(co2)
        vehicle_data["tax_band"] = tax_info["band"]
        vehicle_data["tax_price"] = f"£{tax_info['price']}"
    else:
        vehicle_data["tax_band"] = "Unknown"
        vehicle_data["tax_price"] = "Unknown"

    # ✅ Add engineCapacityInL
    engine_cc = vehicle_data.get("engineCapacity", None)
    if engine_cc is not None:
        # Convert to litres and round to nearest 0.1
        engine_l = round(engine_cc / 1000, 1)
        vehicle_data["engineCapacityInL"] = f"{engine_l:.1f}L"
    else:
        vehicle_data["engineCapacityInL"] = "Unknown"

    # ✅ Final output
    print(json.dumps(vehicle_data, indent=2, ensure_ascii=False))
    return json.dumps(vehicle_data, indent=2, ensure_ascii=False)

# Example usage
data("SH11FAX")
