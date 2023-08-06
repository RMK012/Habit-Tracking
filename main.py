import requests
from datetime import datetime

TOKEN = "205532567@#"
USERNAME = "razmoshe"
GRAPH_ID = "graph1"
today = datetime(year=2023, month=3, day=5)
TODAY = today.strftime("%Y%m%d")


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Swimming Graph",
    "unit": "m",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)


pixel_config = {
    "date": TODAY,
    "quantity": input("How many pools did you swam today?"),

}
data_update = {
    "quantity": "54.2"
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_update_endpoint =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
delete_endpoint =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
#response = requests.put(url=pixel_update_endpoint, json=data_update, headers=headers)
#response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
