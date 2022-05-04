import requests
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ID'
auth_token = 'TOKEN'


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "KEY"

weather_params = {
    "lat" : 7.419325,
    "lon" : 3.970969,
    "appid" : api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="its going to rain today, Remember to take an umbrella.",
        from_='Send Number',
        to='Recive Number'
    )

    print(message.status)
