# API to locate a the longitude and latitude 
#request 
import requests

responce = requests.get(url="http://api.open-notify.org/iss-now.json")
# To check the api responce 
responce.raise_for_status()


# to get data 
data = responce.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

location = (latitude, longitude)
print(location)
