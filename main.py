import requests
import json

def main():
    getToken()
    getCategories()


def getToken():
    url = "https://accounts.spotify.com/api/token"

    payload = "client_id=test_id&client_secret=test_secret&grant_type=client_credentials"
    headers = {
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    JSON_response = response.json()
    accessToken = JSON_response["access_token"]

    print(accessToken)
    print(response.text)
    return accessToken


def getCategories():
    url = "https://api.spotify.com/v1/browse/categories"

    headers = {
        'authorization': "Bearer test_token",
    }

    response = requests.request("GET", url, headers=headers)

    JSON_response = response.json()
    categories = JSON_response["categories"]
    categoriesSimplified = {}
    for categories in categories["items"]:
        print(categories["name"])
        categoriesSimplified[categories["id"]] = categories["name"]

if __name__ == "__main__":
    main()