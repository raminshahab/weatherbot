from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests

class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker):
        url = "http://api.weatherstack.com/current"
        access_key = "4375fd6915057370afea8398ddc7f7c2"
        loc = tracker.get_slot('location')
        params = {'access_key': access_key, 'query': loc}

        r = requests.get(url=url, params=params)
        data = r.json()

        city = data['location']['name']
        condition = data['current']['weather_descriptions']
        temperature_c = data['current']['temperature']
        humidity = data['current']['humidity']
        wind_mph = data['current']['wind_speed']

        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(
            condition, city, temperature_c, humidity, wind_mph)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]
