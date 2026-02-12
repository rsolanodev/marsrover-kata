from dataclasses import dataclass
from enum import StrEnum


class Direction(StrEnum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

    def is_north(self) -> bool:
        return self == Direction.NORTH

    def is_south(self) -> bool:
        return self == Direction.SOUTH

    def is_east(self) -> bool:
        return self == Direction.EAST

    def is_west(self) -> bool:
        return self == Direction.WEST


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
        if self.direction.is_north():
            self.y = self.y + 1
            return

        if self.direction.is_south():
            self.y = self.y - 1
            return

        if self.direction.is_east():
            self.x = self.x + 1
            return

        if self.direction.is_west():
            self.x = self.x - 1
            return

    def backward(self) -> None:
        if self.direction.is_north():
            self.y = self.y - 1
            return

        if self.direction.is_south():
            self.y = self.y + 1
            return

        if self.direction.is_east():
            self.x = self.x - 1
            return

        if self.direction.is_west():
            self.x = self.x + 1
            return

    def left(self) -> None:
        map_next_direction = {
            Direction.NORTH: Direction.WEST,
            Direction.EAST: Direction.NORTH,
            Direction.SOUTH: Direction.EAST,
            Direction.WEST: Direction.SOUTH,
        }
        self.direction = map_next_direction[self.direction]

    def right(self) -> None:
        map_next_direction = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
        }
        self.direction = map_next_direction[self.direction]

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
