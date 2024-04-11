import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN="39182491jffd"
USERNAME="michaelcoll"

users_params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMInor": "yes"
}



# response = requests.post(url=pixela_endpoint, json=users_params)
"""Let's visit https://pixe.la/@michaelcoll """
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#print(graph_endpoint)

graph_config = {
    "id":"graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#create graph
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pxiel_creatiion_url = "https://pixe.la/v1/users/michaelcoll/graphs/graph1"
today = datetime.now()
#print(today.strftime("%Y%m%d"))

data = {"date": today.strftime("%Y%m%d"),
        #"date":"20240405",
        "quantity":"50"
        #"optionalData":"{\"key\":\"value\"}"
        }

#update graph with new pixel
#response = requests.post(url=pxiel_creatiion_url , json=data, headers=headers)

#update existing pixel using put
update_data = {
        "quantity":"200"
        }

pixel_update_url = "https://pixe.la/v1/users/michaelcoll/graphs/graph1/20240405"
response = requests.put(url=pixel_update_url , json=update_data, headers=headers)
print(response.text)

#delete existing pixel using put

pixel_update_url = "https://pixe.la/v1/users/michaelcoll/graphs/graph1/20240405"
response = requests.delete(url=pixel_update_url , headers=headers)
print(response.text)