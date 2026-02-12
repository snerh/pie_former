class CloneState:
    active: bool = True
    branch: int
    end_frame: int | None = None
    def __init__(self, active, branch, end_frame):
        self.active = active
        self.branch = branch
        self.end_frame = end_frame