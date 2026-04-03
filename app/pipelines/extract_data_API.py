import requests



access_token = "..."

url = "https://api.spotify.com/v1/albums"

params = {
    "ids": "43k99CXeU2JUO21G1F4WCP,1aqg30bNvLSWgShZgX4oop,0KJc9ksnoJJsdpQxV3z5i1,2Y9IRtehByVkegoD7TcLfi,3kjHLu1pL7tdY88GFwEkl6,31hcgCSu4mlA82syOFItur,2DQ6hHlAGj6DiT0Y068bnK,5DV2liMHX5AqtiLqy3Qu1b"
}

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(url, headers=headers, params=params)

data = response.json()





