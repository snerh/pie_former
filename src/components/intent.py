class Intent:
    def __init__(self):
        self.move_x = 0      # -1 .. 0 .. 1
        self.jump = False
        self.jump_buffer = 0
        self.clone_pressed = False
        self.clone_buffer = 0
