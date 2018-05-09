from meya import Component
from meya.cards import ImageWithButtons, Button


class CardComponent(Component):
    def start(self):
        # instantiate the card
        image_url = "http://bit.ly/1NPO0xx"
        buttons = [
          Button(text='Cute'),
          Button(text='Not cute'),
          Button(text='Kind of cute')
        ]
        card = ImageWithButtons(image_url=image_url, buttons=buttons, mode="quick_reply")

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=card)

        # respond as you normally would
        return self.respond(message=message, action="next")
