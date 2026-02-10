class Collider:
    def __init__(self, rect, solid=True, one_way=False):
        self.rect = rect
        self.prev_rect = rect
        self.solid = solid
        self.one_way = one_way

    def serialize(self):
         return {
            "x": self.rect.x,
            "y": self.rect.y
        }

    def deserialize(self, data):
        self.rect.x = data["x"]
        self.rect.y = data["y"]