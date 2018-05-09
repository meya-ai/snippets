from meya.cards import Receipt
from meya import Component


class ReceiptComponent(Component):
    def start(self):

        receipt_data = {
            'recipient_name': 'Nikola Tesla',
            'order_number': '123456789',
            'currency': "CAD",
            'payment_method': "Mastercard 1234",
            'order_url': "https://meya.ai/asdfasdf",
            'timestamp': "1465492181",
            'summary': {
                'subtotal': 42.00,
                'total_cost': 45.22
            },
            'elements': [
                {
                  'title': "Red bag flux",
                  'price': 22,
                  'image_url': "http://i.imgur.com/1c3xI4a.jpg"
                },
                {
                  'title': "Blue bag coil",
                  'price': 20,
                }
            ],
            'address': {
                'street_1': "125 Main St.",
                'street_2': "Unit 100",
                'postal_code': "1234562",
                'city': "Megacity",
                'state': "OH",
                'country': "USA",
            },
            'adjustments': [
                {
                  'name': "New customer",
                  'amount': 5.00
                }
            ]
        }

        receipt_card = Receipt(payload=receipt_data)

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=receipt_card)

        # respond as you normally would
        return self.respond(message=message, action="next")
