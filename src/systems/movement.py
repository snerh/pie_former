from settings import PLAYER_MAX_SPEED, PLAYER_ACCEL, PLAYER_FRICTION, JUMP_SPEED, JUMP_BUFFER_TIME
from components.intent import Intent
from components.physics_body import PhysicsBody

class MovementSystem:
    def update(self, entities, dt):
        for e in entities:
            intent = e.get(Intent)
            body = e.get(PhysicsBody)

            if not intent or not body:
                continue

            # горизонтальное движение
            if intent.move_x !=0:
                body.vx = intent.move_x * PLAYER_ACCEL * dt *10
            
            # ограничение скорости
            if body.vx > PLAYER_MAX_SPEED:
                body.vx = PLAYER_MAX_SPEED
            if body.vx < -PLAYER_MAX_SPEED:
                body.vx = -PLAYER_MAX_SPEED

            # прыжок
            intent.jump_buffer -= dt
            if intent.jump:
                intent.jump = False
                intent.jump_buffer = JUMP_BUFFER_TIME

            if intent.jump_buffer > 0 and body.on_ground:
                body.vy = -JUMP_SPEED
                body.on_ground = False
                intent.jump_buffer = 0
                