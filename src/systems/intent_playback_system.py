from components.intent_playback import IntentPlayback
from components.clone_state import CloneState
class IntentPlaybackSystem:
    def update(self, entities, timeline, frame):
        for e in entities:
            play = e.get(IntentPlayback)
            state = e.get(CloneState)

            if not play or not state:
                continue

            branch = state.branch
            play.move_x = 0
            play.jump = False
            play.clone_pressed = False

            if frame not in timeline.branches[branch].intents:
                continue

            data = timeline.branches[branch].intents[frame].get(e.id)

            if data:
                state.active = True
                play.move_x = data["move_x"]
                play.jump = data["jump"]
                play.clone_pressed = data["clone_pressed"]