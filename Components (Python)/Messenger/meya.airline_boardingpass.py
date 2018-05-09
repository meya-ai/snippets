from meyacards import AirlineBoardingPass
from meya import Component


class BoardingPassComponent(Component):
    def start(self):
        BOARDING_PASS = {
            "intro_message": "You are checked in.",
            "locale": "en_US",
            "boarding_pass": [
                {
                    "passenger_name": "SMITH NICOLAS",
                    "pnr_number": "CG4X7U",
                    "travel_class": "business",
                    "seat": "74J",
                    "auxiliary_fields": [
                      {
                          "label": "Terminal",
                          "value": "T1"
                      },
                        {
                          "label": "Departure",
                          "value": "30OCT 19:05"
                      }
                    ],
                    "secondary_fields": [
                        {
                            "label": "Boarding",
                            "value": "18:30"
                        },
                        {
                            "label": "Gate",
                            "value": "D57"
                        },
                        {
                            "label": "Seat",
                            "value": "74J"
                        },
                        {
                            "label": "Sec.Nr.",
                            "value": "003"
                        }
                    ],
                    "logo_image_url": "https://www.example.com/en/logo.png",
                    "header_image_url": "https://www.example.com/en/fb/header.png",
                    "qr_code": "M1SMITH NICOLAS  CG4X7U nawouehgawgnapwi3jfa0wfh",
                    "above_bar_code_image_url": "https://www.example.com/en/PLAT.png",
                    "flight_info": {
                        "flight_number": "KL0642",
                        "departure_airport": {
                            "airport_code": "JFK",
                            "city": "New York",
                            "terminal": "T1",
                            "gate": "D57"
                        },
                        "arrival_airport": {
                            "airport_code": "AMS",
                            "city": "Amsterdam"
                        },
                        "flight_schedule": {
                            "departure_time": "2016-01-02T19:05",
                            "arrival_time": "2016-01-05T17:30"
                        }
                    }
                },
                {
                    "passenger_name": "JONES FARBOUND",
                    "pnr_number": "CG4X7U",
                    "travel_class": "business",
                    "seat": "74K",
                    "auxiliary_fields": [
                        {
                            "label": "Terminal",
                            "value": "T1"
                        },
                        {
                            "label": "Departure",
                            "value": "30OCT 19:05"
                        }
                    ],
                    "secondary_fields": [
                        {
                            "label": "Boarding",
                            "value": "18:30"
                        },
                        {
                            "label": "Gate",
                            "value": "D57"
                        },
                        {
                            "label": "Seat",
                            "value": "74K"
                        },
                        {
                            "label": "Sec.Nr.",
                            "value": "004"
                        }
                    ],
                    "logo_image_url": "https://www.example.com/en/logo.png",
                    "header_image_url": "https://www.example.com/en/fb/header.png",
                    "qr_code": "M1JONES FARBOUND  CG4X7U nawouehgawgnapwi3jfa0wfh",
                    "above_bar_code_image_url": "https://www.example.com/en/PLAT.png",
                    "flight_info": {
                        "flight_number": "KL0642",
                        "departure_airport": {
                            "airport_code": "JFK",
                            "city": "New York",
                            "terminal": "T1",
                            "gate": "D57"
                        },
                        "arrival_airport": {
                            "airport_code": "AMS",
                            "city": "Amsterdam"
                        },
                        "flight_schedule": {
                            "departure_time": "2016-01-02T19:05",
                            "arrival_time": "2016-01-05T17:30"
                        }
                    }
                }
            ]
        }

        boarding_pass_card = AirlineBoardingPass(payload=BOARDING_PASS)

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=card)

        # respond as you normally would
        return self.respond(message=message, action="next")
