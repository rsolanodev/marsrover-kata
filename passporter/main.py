from dataclasses import dataclass
from enum import StrEnum


class Direction(StrEnum):
    N = "N"
    S = "S"
    E = "E"
    W = "W"


class RotateOptions(StrEnum):
    LEFT = "left"
    RIGHT = "right"


@dataclass
class MarsRover:
    x: int
    y: int
    direction: Direction

    def forward(self) -> None:
        if self.direction == Direction.N:
            self.y = self.y + 1
            return

        if self.direction == Direction.S:
            self.y = self.y - 1
            return

        if self.direction == Direction.E:
            self.x = self.x + 1
            return

        if self.direction == Direction.W:
            self.x = self.x - 1
            return

    def backward(self) -> None:
        if self.direction == Direction.N:
            self.y = self.y - 1
            return

        if self.direction == Direction.S:
            self.y = self.y + 1
            return

        if self.direction == Direction.E:
            self.x = self.x - 1
            return

        if self.direction == Direction.W:
            self.x = self.x + 1
            return

    def rotate(self, to: RotateOptions) -> None:
        if to == RotateOptions.LEFT:
            if self.direction == Direction.N:
                self.direction = Direction.W
                return

            if self.direction == Direction.E:
                self.direction = Direction.N
                return

            if self.direction == Direction.S:
                self.direction = Direction.E
                return

            if self.direction == Direction.W:
                self.direction = Direction.S
                return

        if to == RotateOptions.RIGHT:
            if self.direction == Direction.N:
                self.direction = Direction.E
                return

            if self.direction == Direction.E:
                self.direction = Direction.S
                return

            if self.direction == Direction.S:
                self.direction = Direction.W
                return

            if self.direction == Direction.W:
                self.direction = Direction.N
                return
