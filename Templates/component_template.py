from meya import Component


class MyComponent(Component):
    def start(self):
        # Your custom code here
        # example:
        # message = self.create_message(text=text)
        return self.respond(message=None, action="next")
