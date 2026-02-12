import pytest
from passporter.main import Direction, MarsRover, RotateOptions


class TestMarsRover:
    def test_initial_mars_rover(self) -> None:
        mars_rover = MarsRover(x=0, y=0, direction=Direction.N)

        assert mars_rover.x == 0
        assert mars_rover.y == 0
        assert mars_rover.direction == "N"

    @pytest.mark.parametrize(
        "direction, expected_y_position, expected_x_position",
        [
            (Direction.N, 1, 0),
            (Direction.S, -1, 0),
            (Direction.E, 0, 1),
            (Direction.W, 0, -1),
        ],
    )
    def test_moves_rover_to_forward(
        self, direction: Direction, expected_y_position: int, expected_x_position: int
    ) -> None:
        mars_rover = MarsRover(x=0, y=0, direction=direction)

        mars_rover.forward()

        assert mars_rover.y == expected_y_position
        assert mars_rover.x == expected_x_position

    @pytest.mark.parametrize(
        "direction, expected_y_position, expected_x_position",
        [
            (Direction.N, -1, 0),
            (Direction.S, 1, 0),
            (Direction.E, 0, -1),
            (Direction.W, 0, 1),
        ],
    )
    def test_moves_rover_to_backward(
        self, direction: Direction, expected_y_position: int, expected_x_position: int
    ) -> None:
        mars_rover = MarsRover(x=0, y=0, direction=direction)

        mars_rover.backward()

        assert mars_rover.y == expected_y_position
        assert mars_rover.x == expected_x_position

    @pytest.mark.parametrize(
        "direction, expected_direction",
        [
            (Direction.N, Direction.W),
            (Direction.E, Direction.N),
            (Direction.S, Direction.E),
            (Direction.W, Direction.S),
        ],
    )
    def test_rotate_rover_to_left(
        self, direction: Direction, expected_direction: Direction
    ) -> None:
        mars_rover = MarsRover(x=0, y=0, direction=direction)

        mars_rover.rotate(to=RotateOptions.LEFT)

        assert mars_rover.direction == expected_direction

    @pytest.mark.parametrize(
        "direction, expected_direction",
        [
            (Direction.N, Direction.E),
            (Direction.E, Direction.S),
            (Direction.S, Direction.W),
            (Direction.W, Direction.N),
        ],
    )
    def test_rotate_rover_to_right(
        self, direction: Direction, expected_direction: Direction
    ) -> None:
        mars_rover = MarsRover(x=0, y=0, direction=direction)

        mars_rover.rotate(to=RotateOptions.RIGHT)

        assert mars_rover.direction == expected_direction
