import pygame
from settings import TILE_SIZE, PLAYER_FRICTION
from entities.entity import Entity
from components.physics_body import PhysicsBody
from components.collider import Collider

class Box(Entity):
    def __init__(self, x, y):
        super().__init__()
        self.add(PhysicsBody(gravity=True, pushable = True, mass=1.0))
        self.add(Collider(pygame.Rect(x,y,TILE_SIZE,TILE_SIZE)))


    def draw(self, screen, camera):
        color = (150,120,50)
        pygame.draw.rect(
            screen, 
            color, 
            camera.apply(self.get(Collider).rect)
            )

