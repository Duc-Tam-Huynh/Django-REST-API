import requests

endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"  # HTTP Requset
#endpoint = "https://httpbin.org/anything"  # RESR API Request
endpoint =  "http://localhost:8000/api/"


get_response = requests.get(endpoint, json = {"query":"Hello word"}) #HTTP Request

# HTTP Request return HTML
# RESR API HTTP Request return JSON
print(get_response.text)
print(get_response.status_code)


#print(get_response.json())