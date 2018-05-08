from meya import Component
from meya.cards import File


class CardComponent(Component):
    def start(self):
        # instantiate the card
        card = File(url="https://s3.amazonaws.com/meya-static/roosters.pdf")

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=card)

        # respond as you normally would
        return self.respond(message=message, action="next")
