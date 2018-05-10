from meya import Component


class RouteUserType(Component):

    def start(self):
        user_type = self.db.user.get("user_type")
        if user_type == "moderator":
            action = "moderator"
        elif user_type == "admin":
            action = "admin"
        else:
            action = "user"
        return self.respond(action=action)
