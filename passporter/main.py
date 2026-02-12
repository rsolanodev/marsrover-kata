from dataclasses import dataclass
from enum import StrEnum


class Direction(StrEnum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


class Movement(StrEnum):
    FORWARD = "forward"
    BACKWARD = "backward"
    LEFT = "left"
    RIGHT = "right"


@dataclass
class MarsRover:
    x: int
    y: int
    direction: Direction

    def forward(self) -> None:
        if self.direction == Direction.NORTH:
            self.y = self.y + 1
            return

        if self.direction == Direction.SOUTH:
            self.y = self.y - 1
            return

        if self.direction == Direction.EAST:
            self.x = self.x + 1
            return

        if self.direction == Direction.WEST:
            self.x = self.x - 1
            return

    def backward(self) -> None:
        if self.direction == Direction.NORTH:
            self.y = self.y - 1
            return

        if self.direction == Direction.SOUTH:
            self.y = self.y + 1
            return

        if self.direction == Direction.EAST:
            self.x = self.x - 1
            return

        if self.direction == Direction.WEST:
            self.x = self.x + 1
            return

    def left(self) -> None:
        if self.direction == Direction.NORTH:
            self.direction = Direction.WEST
            return

        if self.direction == Direction.EAST:
            self.direction = Direction.NORTH
            return

        if self.direction == Direction.SOUTH:
            self.direction = Direction.EAST
            return

        if self.direction == Direction.WEST:
            self.direction = Direction.SOUTH
            return

    def right(self) -> None:
        if self.direction == Direction.NORTH:
            self.direction = Direction.EAST
            return

        if self.direction == Direction.EAST:
            self.direction = Direction.SOUTH
            return

        if self.direction == Direction.SOUTH:
            self.direction = Direction.WEST
            return

        if self.direction == Direction.WEST:
            self.direction = Direction.NORTH
            return

    def move(self, movements: list[Movement]) -> None:
        for movement in movements:
            if movement == Movement.FORWARD:
                self.forward()
                continue

            if movement == Movement.BACKWARD:
                self.backward()
                continue

            if movement == Movement.LEFT:
                self.left()
                continue

            if movement == Movement.RIGHT:
                self.right()
                continue
