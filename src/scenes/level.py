import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE
from scenes.base import Scene
from entities.player import Player
from entities.platform import Platform
from entities.box import Box
from systems.input import InputSystem
from systems.movement import MovementSystem
from systems.physics import PhysicsSystem
from systems.camera import Camera
from levels.level1 import LEVEL_1

class LevelScene(Scene):
    def __init__(self):
        self.input_system = InputSystem()
        self.movement_system = MovementSystem()
        self.physics_system = PhysicsSystem()
        
        self.player = Player(100,300)
        self.entities = [self.player]

        self.level_width = len(LEVEL_1[0]) * TILE_SIZE
        self.level_height = len(LEVEL_1) * TILE_SIZE

        self.camera = Camera(
            SCREEN_WIDTH, 
            SCREEN_HEIGHT, 
            self.level_width, 
            self.level_height)
            
        for row_index, row in enumerate(LEVEL_1):
            for col_index, cell in enumerate(row):
                if cell == "#":
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    self.entities.append(
                        Platform(x, y, TILE_SIZE, TILE_SIZE, one_way = False)
                    )
                elif cell == "-":
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    self.entities.append(
                        Platform(x, y, TILE_SIZE, TILE_SIZE, one_way = True)
                    )
                elif cell == "B":
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    self.entities.append(
                        Box(x, y)
                    )


    def handle_event(self, event):
        pass

    def update(self, dt):
        self.input_system.update(self.entities)
        self.movement_system.update(self.entities, dt)
        self.physics_system.update(self.entities, dt)
        self.camera.update(self.player)

    def draw(self, screen):
        for entity in self.entities:
            entity.draw(screen, self.camera)


