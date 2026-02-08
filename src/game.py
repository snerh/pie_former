import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR
from scenes.level import LevelScene

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        pygame.display.set_caption("Platformer")
        self.clock = pygame.time.Clock()
        self.scene = LevelScene()

    def run(self):
        running = True
        while running:
            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.scene.handle_event(event)

            self.scene.update(dt)
            self.screen.fill(BG_COLOR)
            self.scene.draw(self.screen)
            pygame.display.flip()

        pygame.quit()

