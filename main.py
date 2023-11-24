# API to locate a the longitude and latitude 
#request 
import requests
from datetime import datetime
from smtplib import *
import time 

email = "enter the email"
password = "enter the password"
MY_LAT = 8.912538
MY_LONG = 77.329895
FORMAT = 0


def is_iss_overhead():
    responce = requests.get(url="http://api.open-notify.org/iss-now.json")
    # To check the api responce 
    responce.raise_for_status()


    # to get data 
    data = responce.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

#within +5 or -5 
    if MY_LAT-5 <= latitude <= MY_LAT-5 and MY_LONG-5 <= longitude <= MY_LONG-5:
        return True
    
def is_night():

    parameter = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : FORMAT

    }


    response = requests.get("https://api.sunrise-sunset.org/json", params= parameter)
    response.raise_for_status()
    data = response.json()
    #print(data)

    sunrise =int(data["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True
    
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection =SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr = email
            to_addrs = "reciver mail"
            msg = "look up"

        )



