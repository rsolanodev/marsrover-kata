import pytest
from passporter.main import Direction, MarsRover, Movement


class TestMarsRover:
    def test_init_mars_rover(self) -> None:
        mars_rover = MarsRover(x=0, y=0, direction=Direction.NORTH)

        assert mars_rover.x == 0
        assert mars_rover.y == 0
        assert mars_rover.direction == "north"

    @pytest.mark.parametrize(
        "direction, expected_y_position, expected_x_position",
        [
            (Direction.NORTH, 1, 0),
            (Direction.SOUTH, -1, 0),
            (Direction.EAST, 0, 1),
            (Direction.WEST, 0, -1),
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
            (Direction.NORTH, -1, 0),
            (Direction.SOUTH, 1, 0),
            (Direction.EAST, 0, -1),
            (Direction.WEST, 0, 1),
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
            (Direction.NORTH, Direction.WEST),
            (Direction.EAST, Direction.NORTH),
            (Direction.SOUTH, Direction.EAST),
            (Direction.WEST, Direction.SOUTH),
        ],
    )
    def test_rotate_rover_to_left(
        self, direction: Direction, expected_direction: Direction
    ) -> None:
        mars_rover = MarsRover(x=0, y=0, direction=direction)

        mars_rover.left()

        assert mars_rover.direction == expected_direction

    @pytest.mark.parametrize(
        "direction, expected_direction",
        [
            (Direction.NORTH, Direction.EAST),
            (Direction.EAST, Direction.SOUTH),
            (Direction.SOUTH, Direction.WEST),
            (Direction.WEST, Direction.NORTH),
        ],
    )
    def test_rotate_rover_to_right(
        self, direction: Direction, expected_direction: Direction
    ) -> None:
        mars_rover = MarsRover(x=0, y=0, direction=direction)

        mars_rover.right()

        assert mars_rover.direction == expected_direction

    def test_moves_mars_rover_around_mars(self) -> None:
        """
        Mars rover in the last stretch reverses to park
        | → → ↓ |
        | ↓ ← ← |
        | ← ← ← |
        """
        mars_rover = MarsRover(x=-1, y=1, direction=Direction.EAST)

        mars_rover.move(
            movements=[
                Movement.FORWARD,
                Movement.FORWARD,
                Movement.RIGHT,
                Movement.FORWARD,
                Movement.RIGHT,
                Movement.FORWARD,
                Movement.FORWARD,
                Movement.LEFT,
                Movement.FORWARD,
                Movement.RIGHT,
                Movement.BACKWARD,
                Movement.BACKWARD,
            ]
        )

        assert mars_rover.x == 1
        assert mars_rover.y == -1
        assert mars_rover.direction == "west"
