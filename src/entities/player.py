import pygame
from entities.entity import Entity
from components.physics_body import PhysicsBody
from components.collider import Collider
from components.intent import Intent
from settings import PLAYER_MAX_SPEED, PLAYER_ACCEL, PLAYER_FRICTION, JUMP_SPEED, JUMP_BUFFER_TIME, TILE_SIZE

class Player(Entity):
    def __init__(self, x, y):
        super().__init__()
        self.add(Intent())
        self.add(PhysicsBody(gravity=True, mass=1.0))
        self.add(Collider(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)))

    def draw(self, screen, camera):
        pygame.draw.rect(
            screen, 
            (200, 200, 50), 
            camera.apply(self.get(Collider).rect)
            )

