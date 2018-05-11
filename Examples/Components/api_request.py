# -*- coding: utf-8 -*-
import requests
from meya import Component


class ChuckNorrisJoke(Component):

    def start(self):
        response = requests.get("http://api.icndb.com/jokes/random")
        text = response.json()['value']['joke']
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
