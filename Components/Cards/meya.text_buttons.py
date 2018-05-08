from meya import Component
from meya.cards import TextWithButtons, Button


class CardComponent(Component):
    def start(self):
        # instantiate the card
        text = 'What is your favorite elelphant?'
        buttons = [
          Button(text='African Elephant'),
          Button(text='Asian Elephant'),
          Button(text='Woolly Mammoth')
        ]
        card = TextWithButtons(text=text, buttons=buttons, mode="quick_reply")

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=card)

        # respond as you normally would
        return self.respond(message=message, action="next")