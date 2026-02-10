import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR, FIXED_DT
from scenes.level import LevelScene
import time

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
        accumulator = 0.0
        prev_time = time.perf_counter()

        while running:
            now = time.perf_counter()
            accumulator += now - prev_time
            prev_time = now
            #dt = self.clock.tick(FPS) / 1000
            while accumulator >= FIXED_DT:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    self.scene.handle_event(event)

                self.scene.update(FIXED_DT)
                self.screen.fill(BG_COLOR)
                self.scene.draw(self.screen)
                pygame.display.flip()

                accumulator -=FIXED_DT

        pygame.quit()

