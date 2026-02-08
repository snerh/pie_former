class Entity:
    def __init__(self):
        self.components = {}

    def add(self, component):
        self.components[type(component)] = component

    def get(self, component_type):
        return self.components.get(component_type)