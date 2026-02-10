import pygame
from entities.entity import Entity
from components.physics_body import PhysicsBody
from components.collider import Collider
from components.intent import Intent
from components.intent_playback import IntentPlayback
from components.clone_state import CloneState
from settings import PLAYER_MAX_SPEED, PLAYER_ACCEL, PLAYER_FRICTION, JUMP_SPEED, JUMP_BUFFER_TIME, TILE_SIZE

class Player(Entity):
    def __init__(self, x, y):
        super().__init__()
        self.add(Intent())
        self.add(PhysicsBody(gravity=True, pushable = True, mass=1.0))
        self.add(Collider(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)))

    def spawn_clone(self, frame):
        rect = self.get(Collider).rect
        clone = Player(rect.x, rect.y)
        print("Clone spowned, id = ", clone.id)
        print(f"Clone spowned, x = {rect.x}, y = {rect.y}")
        self.components = {}
        self.add(IntentPlayback())
        self.add(PhysicsBody(gravity=True, pushable = True, mass=1.0))
        self.add(Collider(pygame.Rect(rect.x, rect.y, TILE_SIZE, TILE_SIZE)))
        self.add(CloneState(True, frame))
        return clone

    def draw(self, screen, camera):
        if self.get(CloneState):
            color = (150, 150, 70)
            if not self.get(CloneState).active:
                return ()
        else:
            color = (200, 200, 50)

        if self.get(Collider):
            pygame.draw.rect(
                screen, 
                color, 
                camera.apply(self.get(Collider).rect)
                )

