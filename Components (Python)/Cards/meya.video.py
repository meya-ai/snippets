from meya import Component
from meya.cards import Video


class CardComponent(Component):
    def start(self):
        # instantiate the card
        video_card = Video(url="https://s3.amazonaws.com/meya-static/aurora-borealis.mp4")

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=card)

        # respond as you normally would
        return self.respond(message=message, action="next")
