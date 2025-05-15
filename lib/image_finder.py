import requests

def get_image_url_from_description(description):
    API_URL = "https://api.unsplash.com/search/photos"
    ACCESS_KEY = "2cD5u48VPw7EzZnDQKKRkyILRNRFZqbWmzkatAxV5cw"

    params = {
        "query": description,
        "client_id": ACCESS_KEY,
        "orientation": "landscape",
        "per_page": 1  # Only want one result
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()  # data is a dict
        results = data.get("results", [])  # safely get the list
        if results:
            return results[0]["urls"]["regular"]
        else:
            print("No results found for:", description)
            return None
    else:
        print("Error fetching image:", response.status_code, response.text)
        return None
