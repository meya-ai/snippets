from meya import Component


class LogFromComponent(Component):
    def start(self):
        context = "My context"
        type = "misc"
        status = "info"
        self.log(context, type=type, status=status)

        return self.respond(action="next")
