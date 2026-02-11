from components.timeline import Timeline
from components.intent import Intent
class IntentRecordSystem:
    def update(self, entities, timeline, branch_id, frame):
        for e in entities:
            intent = e.get(Intent)

            if not intent:
                continue

            timeline.intents\
                .setdefault(branch_id, {})\
                .setdefault(frame, {})[e.id] = {"move_x":intent.move_x, 
                                                "jump":intent.jump, 
                                                "clone_pressed":intent.clone_pressed}
            #.append((intent.move_x, intent.jump))