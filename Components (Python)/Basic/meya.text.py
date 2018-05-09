from meya import Component


class TextComponent(Component):
    def start(self):
        text = "My text"

        # create the message
        message = self.create_message(text=text)

        # respond as you normally would
        return self.respond(message=message, action="next")
