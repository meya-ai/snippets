from meyacards import AirlineCheckin
from meya import Component


class AirlineCheckinComponent(Component):
    def start(self):
        CHECKIN = {
            "intro_message": "Check-in is available now.",
            "locale": "en_US",
            "pnr_number": "ABCDEF",
            "flight_info": [
                {
                    "flight_number": "f001",
                    "departure_airport": {
                      "airport_code": "SFO",
                      "city": "San Francisco",
                      "terminal": "T4",
                      "gate": "G8"
                    },
                    "arrival_airport": {
                        "airport_code": "SEA",
                        "city": "Seattle",
                        "terminal": "T4",
                        "gate": "G8"
                    },
                    "flight_schedule": {
                        "boarding_time": "2016-01-05T15:05",
                        "departure_time": "2016-01-05T15:45",
                        "arrival_time": "2016-01-05T17:30"
                    }
                }
            ],
            "checkin_url": "https://www.airline.com/check-in"
        }

        checkin_card = AirlineCheckin(payload=CHECKIN)

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=checkin_card)

        # respond as you normally would
        return self.respond(message=message, action="next")
