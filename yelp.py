import requests

path = "https://api.yelp.com/v3/businesses/search"

YELP_API_KEY = "UKb5ZJ97SAYUY68WJvSY50q7jbI_UK4iwfOPPqZphtbtF7P0t2JJVvW7fd8yj-nltwTpg56FFd7O0vgy8NpfSYZl-Xq3XHEkDUiy50yXT0Fe1R7Bc3U8nI-QC4SXY3Yx"

query_params = {
    "location": "New York City",
    "term": "Szechuan",
    "attributes": "hot_and_new",
}

headers = {"Authorization": f"Bearer {YELP_API_KEY}"}

response = requests.get(path, params=query_params, headers=headers)
response_text = response.json()
restaurants = response_text["businesses"]
print(response)

for restaurant in restaurants:
    print(restaurant["name"])