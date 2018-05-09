from meya import Component
from meya.cards import Card, Button


class CardComponent(Component):
    def start(self):
        # instantiate the card
        title = "Elephants are big"
        text = "They are really big sometimes."
        image_url = "http://bit.ly/1NPO0xx"
        buttons = [
          Button(text='Agreed'),
          Button(text='Whales are bigger')
        ]
        card = Card(title=title,
                    text=text,
                    image_url=image_url,
                    buttons=buttons)

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=card)

        # respond as you normally would
        return self.respond(message=message, action="next")
