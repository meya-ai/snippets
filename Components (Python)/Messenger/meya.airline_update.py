from meyacards import AirlineUpdate
from meya import Component


class AirlineUpdateComponent(Component):
    def start(self):
        UPDATE = {
            "intro_message": "Your flight is delayed",
            "update_type": "delay",
            "locale": "en_US",
            "pnr_number": "CF23G2",
            "update_flight_info": {
                "flight_number": "KL123",
                "departure_airport": {
                    "airport_code": "SFO",
                    "city": "San Francisco",
                    "terminal": "T4",
                    "gate": "G8"
                },
                "arrival_airport": {
                    "airport_code": "AMS",
                    "city": "Amsterdam",
                    "terminal": "T4",
                    "gate": "G8"
                },
                "flight_schedule": {
                    "boarding_time": "2015-12-26T10:30",
                    "departure_time": "2015-12-26T11:30",
                    "arrival_time": "2015-12-27T07:30"
                }
            }
        }

        update_card = AirlineUpdate(payload=UPDATE)

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=update_card)

        # respond as you normally would
        return self.respond(message=message, action="next")
