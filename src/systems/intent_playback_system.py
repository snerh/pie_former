from components.intent_playback import IntentPlayback
class IntentPlaybackSystem:
    def update(self, entities, timeline, frame):
        for e in entities:
            play = e.get(IntentPlayback)

            if not play:
                continue
            play.move_x = 0
            play.jump = False
            play.clone_pressed = False

            if frame not in timeline.intents:
                return    

            data = timeline.intents[frame].get(e.id)

            if data:
                #print(f"frame {frame}, id = {e.id}, data = move_x:{data["move_x"]}, junp:{data["jump"]}")
                play.move_x = data["move_x"]
                play.jump = data["jump"]
                play.clone_pressed = data["clone_pressed"]