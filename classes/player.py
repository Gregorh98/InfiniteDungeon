from exceptions.player import InvalidDirectionException
from lookups import Directions


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.inventory = {}
        self.hp = 100
        self.inCombat = False

    @property
    def coords(self):
        return ((self.x, self.y))


    def move(self, direction):
        match (direction):
            case Directions.North:
                self.y -= 1
            case Directions.South:
                self.y += 1
            case Directions.East:
                self.x += 1
            case Directions.West:
                self.y -= 1
            case _:
                raise InvalidDirectionException(direction)

    def goto(self, x, y):
        if not isinstance(x, int):
            raise TypeError(f"Invalid X parameter. Expected int, got {type(x).__name__}")

        if not isinstance(x, int):
            raise TypeError(f"Invalid Y parameter. Expected int, got {type(y).__name__}")

        self.x = x
        self.y = y



