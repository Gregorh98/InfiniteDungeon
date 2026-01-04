from lookups import Directions


def InvalidDirectionException(d):
    raise Exception(f"Requested direction {d} is not one of {Directions.North, Directions.South, Directions.East, Directions.West}. Use Directions module to access valid direction strings (E.g. Directions.North)")
