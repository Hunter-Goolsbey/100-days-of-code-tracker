import requests
from datetime import datetime
import os


USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = "graph1"


##Standard Pixela Endpoint
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
#response = requests.post(url=pixela_endpoint, json=user_params)


##CREATE NEW GRAPH ENDPOINT
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "My Coding Graph",
    "unit": "Hrs",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


##CREATE PIXEL
today = datetime.now().strftime("%Y%m%d")
print(today)

pixel_data = {
    "date": today,
    "quantity": input("How many Hours did you spend coding today?: ")
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
new_pixel_data = {
    "quantity": "1.5"
}

#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)


##DELETE ENDPOINT
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
#response = requests.delete(url=delete_endpoint, headers=headers)


print(response.text)
