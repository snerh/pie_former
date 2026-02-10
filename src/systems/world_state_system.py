from entities.world_snapshot import WorldSnapshot
class WorldStateSystem:
    def snapshot(self, entities):
        data = []
        for e in entities:
            comp_data = {}
            for c in e.components.values():
                if hasattr(c, "serialize"):
                    comp_data[type(c).__name__] = c.serialize()

            data.append({
                "id": e.id,
                "components": comp_data
            })
        print("World saved!")
        return WorldSnapshot(data)

    def load_snapshot(self, snapshot, entities):
        entities_by_id = {e.id: e for e in entities}

        for e_data in snapshot.entities_data:
            e = entities_by_id[e_data["id"]]

            for c_name, c_data in e_data["components"].items():
                comp = next(
                    c for c in e.components.values()
                    if type(c).__name__ == c_name
                )
                comp.deserialize(c_data)
    
