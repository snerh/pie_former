import pygame
from components.intent import Intent
class InputSystem:
    def update(self, entities):
        keys = pygame.key.get_pressed()

        for e in entities:
            intent = e.get(Intent)
            if not intent:
                continue

            intent.move_x = 0
            intent.jump = False

            if keys[pygame.K_LEFT]:
                intent.move_x -= 1
            if keys[pygame.K_RIGHT]:
                intent.move_x += 1
            if keys[pygame.K_SPACE]:
                intent.jump = True
