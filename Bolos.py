class Roll:
    def __init__(self, pins: int):
        self.pins = pins

class Frame:
    def __init__(self):
        self.rolls = []

    def add_roll(self, pins: int):
        self.rolls.append(Roll(pins))

    def score(self) -> int:
        frame_score = 0
        for roll in self.rolls:
            frame_score += roll.pins
        return frame_score

    def is_spare(self) -> bool:
        if len(self.rolls) == 2 and self.score() == 10:
            return True
        return False

    def is_strike(self) -> bool:
        if len(self.rolls) == 1 and self.score() == 10:
            return True
        return False

class NormalFrame(Frame):
    pass

class TenthFrame(Frame):
    def add_roll(self, pins: int):
        if len(self.rolls) < 2:
            super().add_roll(pins)

class Game:
    def __init__(self):
        self.frames = []

    def roll(self, pins: int):
        if not self.frames or len(self.frames[-1].rolls) == 2 or self.frames[-1].is_strike():
            if len(self.frames) < 10:
                self.frames.append(NormalFrame())
            else:
                self.frames.append(TenthFrame())
        self.frames[-1].add_roll(pins)

    def score(self) -> int:
        pass

