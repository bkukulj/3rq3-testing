class MenuItem:
    def __init__(self, name):
        self.name = name
        self.valid = True
        self.price = 1.5

    def invalidate_item(self):
        self.valid = False
