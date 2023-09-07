

class GameIdProvider:
    def __init__(self):
        self.counter = -1

    def get_new_id(self):
        self.counter += 1
        return self.counter
        