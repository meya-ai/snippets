from meya import Component
from meya.cards import Image


class CardComponent(Component):
    def start(self):
        # instantiate the card
        card = Image(image_url="http://bit.ly/1NPO0xx")

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=card)

        # respond as you normally would
        return self.respond(message=message, action="next")
