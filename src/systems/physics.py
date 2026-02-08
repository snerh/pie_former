from settings import GRAVITY, PLAYER_FRICTION
from components.physics_body import PhysicsBody
from components.collider import Collider

class PhysicsSystem:
    def update(self, entities, dt):
        solids = entities
        for e in entities:
            body = e.get(PhysicsBody)
            col = e.get(Collider)

            if not body or not col:
                continue
            col.prev_rect = col.rect.copy()
            self.apply_gravity(body, dt)
            self.apply_friction(body, dt)
            self.move_x(e, solids, dt)
            self.move_y(e, solids, dt)
            

    def apply_gravity(self, body, dt):
        if body.gravity:
            body.vy += GRAVITY * dt
    
    def apply_friction(self, body, dt):
        if body.vx > 0 and body.on_ground:
            body.vx -= PLAYER_FRICTION * dt
            if body.vx < 0:
                body.vx =0
        elif body.vx < 0 and body.on_ground:
            body.vx += PLAYER_FRICTION * dt
            if body.vx > 0:
                body.vx =0

    def move_x(self, entity, solids, dt):
        body = entity.get(PhysicsBody)
        col = entity.get(Collider)

        col.rect.x += body.vx * dt

        for s in solids:
            if s is entity:
                continue
            sc = s.get(Collider)
            sb = s.get(PhysicsBody)
            if not sb:
                svx = 0
            else:
                svx = sb.vx

            if not sc or not sc.solid or sc.one_way:
                continue
            if col.rect.colliderect(sc.rect):
                if sb and sb.pushable:
                    sb.vx = body.vx
                if body.vx > 0:
                    col.rect.right = sc.rect.left
                elif body.vx < 0:
                    col.rect.left = sc.rect.right
                body.vx = svx
    
    def move_y(self, entity, solids, dt):
        body = entity.get(PhysicsBody)
        col = entity.get(Collider)

        col.rect.y += body.vy * dt
        body.on_ground = False

        for s in solids:
            if s is entity:
                continue
            sc = s.get(Collider)
            sb = s.get(PhysicsBody)
            if not sb:
                svy = 0
            else:
                svy = sb.vy

            if not sc or not sc.solid:
                continue

            if col.rect.colliderect(sc.rect):
                # толкаем ящик solid
                if sb and sb.pushable:
                    sb.vy = body.vy
                # удар сверху    
                if (
                    col.prev_rect.bottom <= sc.rect.top
                    and col.rect.bottom > sc.rect.top
                ):
                    col.rect.bottom = sc.rect.top
                    body.vy = svy
                    body.on_ground = True
                    if body.pushable and sb:
                        body.vx = sb.vx
                
                # удар снизу
                elif (
                    col.prev_rect.top >= sc.rect.bottom
                    and col.rect.top < sc.rect.bottom
                    and not sc.one_way # не односторонняя платформа!
                ):
                    col.rect.top = sc.rect.bottom
                    body.vy = svy

                #  удар сверху
                #if body.vy >= 0:
                #    col.rect.bottom = sc.rect.top
                #    if body.pushable and sb:
                #        body.vx = sb.vx
                #    body.on_ground = True
                # удар снизу
                #elif body.vy < 0 and not sc.one_way:
                #    col.rect.top = sc.rect.bottom
                #body.vy = svy



def vertical_collisions(entity, solids):
    entity.on_ground = False

    for platform in solids:
        if not platform.solid:
            continue
        if not entity.rect.colliderect(platform.rect):
            continue
        
        # удар сверху    
        if (
            entity.prev_rect.bottom <= platform.rect.top
            and entity.rect.bottom > platform.rect.top
        ):
            entity.rect.bottom = platform.rect.top
            entity.vel_y = 0
            entity.on_ground = True
        
        # удар снизу
        elif (
            entity.prev_rect.top >= platform.rect.bottom
            and entity.rect.top < platform.rect.bottom
            and not platform.one_way # не односторонняя платформа!
        ):
            entity.rect.top = platform.rect.bottom
            entity.vel_y = 0
            


def horizontal_collisions(entity, solids):
    for platform in solids:
        if (not entity.rect.colliderect(platform.rect)) or platform.one_way:
            continue

        # толкаем коробку 
        if platform.pushable:
            platform.vel_x = entity.vel_x 
            

        # удар слева
        elif (
            entity.prev_rect.right <= platform.rect.left
            and entity.rect.right > platform.rect.left
        ):
            entity.rect.right = platform.rect.left
            entity.vel_x = 0

        # удар справа
        elif (
            entity.prev_rect.left >= platform.rect.right
            and entity.rect.left < platform.rect.right
        ):
            entity.rect.left = platform.rect.right
            entity.vel_x = 0
