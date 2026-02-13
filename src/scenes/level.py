import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE, FIXED_DT
from scenes.base import Scene
from entities.player import Player
from entities.platform import Platform
from entities.box import Box
from systems.input import InputSystem
from systems.movement import MovementSystem
from systems.physics import PhysicsSystem
from systems.intent_playback_system import IntentPlaybackSystem
from systems.intent_record_system import IntentRecordSystem
from systems.world_state_system import WorldStateSystem
from systems.clone_spawn_system import CloneSpawnSystem
from systems.clone_lifecycle_system import CloneLifecycleSystem
from components.timeline import Timeline, Branch
from systems.camera import Camera
from levels.level1 import LEVEL_1

class LevelScene(Scene):
    def __init__(self):
        self.frame = 0
        self.branch_id = 0
        self.timeline = Timeline()
        self.input_system = InputSystem()
        self.record_system = IntentRecordSystem()
        self.playback_system = IntentPlaybackSystem()
        self.clone_spawn_system = CloneSpawnSystem()
        self.clone_lifecycle_system = CloneLifecycleSystem()
        self.movement_system = MovementSystem()
        self.physics_system = PhysicsSystem()
        self.world_state_system = WorldStateSystem()
        
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
        # если создали клона, откатываем мир назад
        self.record_system.update(self.entities, self.timeline, self.branch_id, self.frame)
        self.clone_lifecycle_system.update(self.entities, self.timeline, self.frame)
        clone = self.clone_spawn_system.update(self.entities, self.timeline, self.branch_id, self.frame, dt)
        
        self.playback_system.update(self.entities, self.timeline, self.frame)
        self.movement_system.update(self.entities, dt) 
        self.physics_system.update(self.entities, dt)
        self.camera.update(self.player)

        
        self.frame +=1

        if clone:
            self.reply_to(self.frame-120)
            self.branch_id += 1
            self.timeline.branches[self.branch_id]=Branch()
            self.entities.append(clone)
            self.player = clone
            snapshot = self.world_state_system.snapshot(self.entities)
            self.timeline.branches[self.branch_id].keyframes.append((self.frame, snapshot))
            self.timeline.branches[self.branch_id].parent_branch = self.branch_id-1
            self.timeline.branches[self.branch_id].fork_frame=self.frame
        
        if self.frame % self.timeline.keyframe_interval == 1:
            snapshot = self.world_state_system.snapshot(self.entities)
            self.timeline.branches[self.branch_id].keyframes.append((self.frame, snapshot))
            
        #self.frame +=1

    def reply_to(self, target_frame):
        # Возвращаем в прошлое весь мир
        keyframe_frame, snapshot = self.timeline.find_keyframe(target_frame)
        self.world_state_system.load_snapshot(snapshot, self.entities)
        print("Old frame = ", self.frame)
        self.frame = keyframe_frame#+1 
        print("New frame = ", self.frame)
        # Проигрываем запись из Timeline до target_frame
        while self.frame < target_frame:
            #print("Loop frame = ", self.frame)
            self.record_system.update(self.entities, self.timeline, self.branch_id, self.frame)
            self.clone_lifecycle_system.update(self.entities, self.timeline, self.frame)
            self.playback_system.update(self.entities, self.timeline, self.frame)
            self.movement_system.update(self.entities, FIXED_DT)
            self.physics_system.update(self.entities, FIXED_DT)
            self.frame +=1
            #self.update(FIXED_DT)
        print("New frame = ", self.frame)

    def draw(self, screen):
        for entity in self.entities:
            entity.draw(screen, self.camera)
