class CloneState:
    active: bool = True
    end_frame: int | None = None
    def __init__(self, active, end_frame):
        self.active = active
        self.end_frame = end_frame