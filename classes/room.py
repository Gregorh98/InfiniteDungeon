from lookups import LightLevel, RoomSize


class Room:
    def __init__(self, root, x, y, descriptor, size=RoomSize.Medium, additional_description_detail=None, enemies=None, loot=None, light_level=LightLevel.BRIGHT, is_interior=False):
        self._root = root
        self._x = x
        self._y = y
        self._descriptor = descriptor
        self._size = size
        self._additional_description_detail = additional_description_detail
        self._enemies = [] if enemies is None else enemies
        self._loot = [] if loot is None else loot
        self._light_level = light_level
        self._is_interior = is_interior

    @property
    def light_level(self):
        if self._is_interior:
            return self._light_level
        else:
            return self._root.light_level

    @property
    def description(self):
        return f"You are standing in a {self._size.name.lower()}, {self.light_level}, {self._descriptor}. {self._additional_description_detail}."

    @property
    def coords(self):
        return ((self._x, self._y))

    @property
    def enemy_count(self):
        return len(self.enemies)

    @property
    def enemies(self):
        return self._enemies

    @property
    def loot(self):
        return self._loot

    def _get_enemy_description_string(self):
        return f"You can {"hear" if self.light_level <= LightLevel.DARK else "see"} {self.enemy_count} enemies"
