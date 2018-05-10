from meya import Component
from time import time


class CheckLastSeen(Component):
    
    def start(self):
        last_seen = self.db.user.get("last_seen")
        if time() - last_seen > 120:
            action = "inactive"
        else:
            action = "active"
        return self.respond(action=action)
