from meya import Component


class MyComponent(Component):
    def start(self):
        return self.respond(message=None, action="next")
