from components.clone_state import CloneState
from components.collider import Collider
from components.physics_body import PhysicsBody
class CloneLifecycleSystem:
    def update(self, entities, timeline, frame):
        for e in entities:
            state = e.get(CloneState)
            if not state:
                continue
            spawn_frame = timeline.spawns.get(frame)
            if spawn_frame:
                spawn_event=spawn_frame.get(e.id)
                if spawn_event:
                    e.get(Collider).deserialize(spawn_event.initial_state["collider"])
                    e.get(PhysicsBody).deserialize(spawn_event.initial_state["body"])
                    state.active = True

            if not state.active:
                continue

            if frame >= state.end_frame:
                print(f"Deactivate clone {e.id}")
                state.active = False
