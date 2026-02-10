class Entity:
    _next_id = 0

    def __init__(self):
        self.id = Entity._next_id
        Entity._next_id += 1
        self.components = {}

    def add(self, component):
        self.components[type(component)] = component

    def get(self, component_type):
        return self.components.get(component_type)

    def disable(self):
        self.components={}