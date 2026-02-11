from components.intent import Intent
from components.collider import Collider
from components.physics_body import PhysicsBody
from components.timeline import Timeline, SpawnEvent
from settings import CLONE_BUFFER_TIME
class CloneSpawnSystem:
    def update(self, entities, timeline, branch_id, frame, dt):
        for e in entities:
            intent = e.get(Intent)
            if not intent:
                continue
            intent.clone_buffer += dt
            # clone spawn
            if intent.clone_pressed and intent.clone_buffer > CLONE_BUFFER_TIME:
                intent.clone_buffer = 0
                clone = e.spawn_clone(frame)
                timeline.spawns.setdefault(frame,{})
                timeline.spawns[frame][clone.id]=SpawnEvent(
                    {
                        "collider": clone.get(Collider).serialize(),
                        "body": clone.get(PhysicsBody).serialize()
                    }
                    )
            #.append((intent.move_x, intent.jump))

                return clone