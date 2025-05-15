import requests

def get_image_url_from_search(query):
    API_URL = "https://api.unsplash.com/search/photos"
    ACCESS_KEY = "2cD5u48VPw7EzZnDQKKRkyILRNRFZqbWmzkatAxV5cw"

    params = {
        "query": query,
        "client_id": ACCESS_KEY,
        "orientation": "landscape",
        "per_page": 30
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return [result["urls"]["regular"] for result in data.get("results", [])]
    else:
        print("Error:", response.status_code, response.text)
        return []
