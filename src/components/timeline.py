class Timeline:
    def __init__(self, keyframe_interval=300):
        self.keyframes = []   # [(frame_index, snapshot)]
        self.intents = {}     # [(frame_index, intent)]
        self.keyframe_interval = keyframe_interval

    def find_keyframe(self, frame):
        for kf in self.keyframes:
            snapframe, snapshot = kf
            if snapframe < frame and snapframe + self.keyframe_interval >= frame:
                return kf
