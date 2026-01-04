from classes import Player
from classes.room import Room
from lookups import RoomSize, Directions

p = Player()
r = Room(object,0, 0, "clearing", RoomSize.Large, "Trees surround it, and the long grass that covers the ground it sways gently in the wind", None, None, is_interior=True)


def process_command(command):
    command = command.lower().split()
    print(command)

    # Check if any of the words are in the command
    if any(word in command for word in ["go", "move"] + Directions.all_direction_strings):

        if any(word in command for word in Directions.north_direction_strings):
            p.move(Directions.north)

        if any(word in command for word in Directions.south):
            p.move(Directions.south)

        if any(word in command for word in Directions.east):
            p.move(Directions.east)

        if any(word in command for word in Directions.west):
            p.move(Directions.west)
while True:
    print(r.description)
    print(p.coords)
    command = input("What do you do? >>")
    process_command(command)

