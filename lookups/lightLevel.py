from enum import IntEnum


class LightLevel(IntEnum):
    PITCH_BLACK = -2
    DARK = -1
    BRIGHT = 0
    VERY_BRIGHT = 1

    def __str__(self) -> str:
        """Return a human-readable name (e.g. 'pitch black')."""
        match self:
            case self.DARK:
                return "dimly lit"
            case self.BRIGHT:
                return "brightly lit"
            case _:
                return self.name.replace("_", " ").lower()