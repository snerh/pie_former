import pygame
from entities.entity import Entity
from components.collider import Collider

class Platform(Entity):
    def __init__(self, x, y, w, h, one_way=False):
        super().__init__()
        self.add(Collider(pygame.Rect(x, y, w, h), solid = True, one_way=one_way))

    def draw(self, screen, camera):
        color = (100,150,100) if self.get(Collider).one_way else (100,100,100)
        pygame.draw.rect(
            screen, 
            color, 
            camera.apply(self.get(Collider).rect)
            )

