import smtplib

import requests
from datetime import datetime

MY_LAT = -26.101749 # Your latitude
MY_LONG = 27.771509 # Your longitude
MY_EMAIL = "tristanpythontest@gmail.com"
MY_PASS = "jbsruwddmdfydfpu"


def is_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (iss_longitude in range(int(MY_LONG)-5, int(MY_LONG)+5) and
            iss_latitude in range(int(MY_LAT)-5, int(MY_LAT)+5)):
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    # print(time_now.hour)

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


if is_dark() and is_iss():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:LOOK UP!!\n\nIf you look up right now, you will be able to see the "
                f"International Space Station!! HOW COOL!!")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASS)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:LOOK UP!!\n\nIf you look up right now, you will be able to see the "
            f"International Space Station!! HOW COOL!!")
