from meya import Component
from meya.cards import TextWithButtons, Button


class CardComponent(Component):
    def start(self):
        # instantiate the card
        text = 'What is your favorite elelphant?'
        buttons = [
          Button(text='African Elephant', action="next"),
          Button(text='Asian Elephant', action="next"),
          Button(text='Woolly Mammoth', action="extinct")
        ]
        card = TextWithButtons(text=text, buttons=buttons, mode="buttons")

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=card)

        # respond as you normally would
        return self.respond(message=message, action="next")
