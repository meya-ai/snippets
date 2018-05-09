from meya import Component


class HelloWorld(Component):

    def start(self):
        text = "Hello, world!"
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
