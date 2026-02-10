class PhysicsBody:
    def __init__(self, gravity=True, pushable=False, mass=1.0):
        self.vx = 0
        self.vy = 0
        self.gravity = gravity
        self.pushable = pushable
        self.mass = mass
        self.on_ground = False

    def serialize(self):
        return {
            "vx": self.vx,
            "vy": self.vy,
            "on_ground": self.on_ground
        }
        
    def deserialize(self, data):
        self.vx = data["vx"]
        self.vy = data["vy"]
        self.on_ground = data["on_ground"]
