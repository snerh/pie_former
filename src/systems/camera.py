from components.collider import Collider

class Camera:
    def __init__(self, screen_w, screen_h, level_w, level_h):
        self.x = 0
        self.y = 0
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.level_w = level_w
        self.level_h = level_h

    def update(self, target):
        col = target.get(Collider)
        self.x = col.rect.centerx - self.screen_w // 2
        if self.x < 0:
            self.x = 0
        elif self.x > self.level_w - self.screen_w:
            self.x = self.level_w - self.screen_w

    def apply(self, rect):
        return rect.move(-self.x, -self.y)
