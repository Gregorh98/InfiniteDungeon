from classes import Player
from classes.room import Room
from lookups import Directions, RoomSize

p = Player()
r = Room(object,0, 0, "clearing", RoomSize.Large, "Trees surround the field, and the long grass sways in the wind.", None, None, is_interior=True)

print(r.description)
print(p.coords)