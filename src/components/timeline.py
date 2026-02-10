class Timeline:
    def __init__(self, keyframe_interval=300):
        self.keyframes = []   # [(frame_index, snapshot)]
        self.intents = {}     # [(frame_index, intent)]
        self.spawns = {}     # [(frame_index, SpawnEvent dict)]
        self.keyframe_interval = keyframe_interval

    def find_keyframe(self, frame):
        for kf in reversed(self.keyframes):
            snapframe, snapshot = kf
            if snapframe < frame and snapframe + self.keyframe_interval >= frame:
                return kf

class SpawnEvent:
    initial_state: dict
    def __init__(self, state):
        self.initial_state = state
