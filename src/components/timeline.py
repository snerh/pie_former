#class Timeline:
#    branches: dict[int, Branch]

#class Branch:
#    intents: dict[int, dict[int, IntentData]]
#    keyframes: dict[int, WorldSnapshot]
#    parent_branch: int | None
#    fork_frame: int | None

class Branch:
    def __init__(self):
        self.keyframes = []   # [(frame_index, snapshot)]
        self.intents = {}     # [(frame_index, intent)]
        self.spawns = {}     # [(frame_index, SpawnEvent dict)]

class Timeline:

    def __init__(self, keyframe_interval=300):
        self.branches = {}
        self.keyframe_interval = keyframe_interval
        
    def find_keyframe(self, frame):
        for branch_id in reversed(self.branches):
            branch = self.branches[branch_id]
            for kf in reversed(branch.keyframes):
                snapframe, snapshot = kf
                if snapframe < frame:
                    return kf

class SpawnEvent:
    initial_state: dict
    def __init__(self, state):
        self.initial_state = state
