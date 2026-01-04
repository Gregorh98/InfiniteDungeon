from lookups import Directions


def InvalidDirectionException(d):
    raise Exception(f"Requested direction {d} is not one of {Directions.north, Directions.south, Directions.east, Directions.west}. Use Directions module to access valid direction strings (E.g. Directions.north)")
