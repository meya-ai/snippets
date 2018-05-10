from meya import Component
from time import time


class UpdateLastSeen(Component):
    
    def start(self):
        self.db.user.set("last_seen", time())
        return self.respond(action="next")