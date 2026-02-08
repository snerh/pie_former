class Intent:
    def __init__(self):
        self.move_x = 0      # -1 .. 0 .. 1
        self.jump = False
        self.jump_buffer = 0
