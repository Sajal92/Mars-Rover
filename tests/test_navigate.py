import pytest
from app.navigate import MarsRover


class TestMarsRover:

    def test_cases(self):
        """
        Tests if the class returns correct output for invalid cases
        """
        inp = {"Rover 1 Command": "LMLMLMLMM", "Rover 1 State": "1 2 N",
               "Rover 2 Command": "MMRMMRMRRM", "Rover 2 State": "3 3 E", "Upper-Right Coordinate": "5 5"}

        tst = MarsRover(inp)
        msg = tst.run()
        msg = ''.join(msg)

        assert ('1 3 N' in msg and '5 1 E' in msg)

    def test_lowercase_entries(self):
        """
        Tests if the class passes lowercase entries
        """
        # Input
        inp = {"Rover 1 Command": "LMLMLMLmm", "Rover 1 State": "1 2 n",
               "Upper-Right Coordinate": "5 5"}

        tst = MarsRover(inp)
        msg = tst.run()[0]

        assert '1 3 N' in msg

    def test_command_with_spaces(self):
        """
        Tests if the class passes whitespace entries in rover commands
        """

        inp = {"Rover 1 Command": "LMLMLMLM M", "Rover 1 State": "1 2 N",
               "Upper-Right Coordinate": "5 5"}

        tst = MarsRover(inp)
        msg = tst.run()[0]

        assert '1 3 N' in msg

    def test_missing_entries1(self):
        """
        Tests if the class returns error message for missing entries
        """

        inp = {"Rover 1 Command": "LMLMLMLMM", "Rover 1 State": "1 2 N",
               "Upper-Right Coordinate": ""}

        tst = MarsRover(inp)
        msg = tst.run()[0]

        assert ('Error' in msg and 'Missing' in msg)

    def test_missing_entries2(self):
        """
        Tests if the class returns error message for missing entries
        (some more cases)
        """

        inp = {"Rover 1 Command": "LMLMLMLMM", "Rover 1 State": "",
               "Upper-Right Coordinate": "5 5"}

        tst = MarsRover(inp)
        msg = tst.run()[0]

        assert ('Error' in msg and 'Missing' in msg)

    def test_invalid_string1(self):
        """
        Tests if the class returns error message for invalid entries
        """
        inp = {"Rover 1 Command": "LMLMLMLMMP", "Rover 1 State": "1 2 N",
               "Upper-Right Coordinate": "5 5"}

        tst = MarsRover(inp)
        msg = tst.run()[0]

        assert ('Error' in msg and 'Invalid entries' in msg)

    def test_invalid_string2(self):
        """
        Tests if the class returns error message for invalid entries
        """

        inp = {"Rover 1 Command": "LMLMLMLMM", "Rover 1 State": "1 2 NS",
               "Upper-Right Coordinate": "5 5"}

        tst = MarsRover(inp)
        msg = tst.run()[0]

        assert ('Error' in msg and 'Invalid entries' in msg)

    def test_invalid_order(self):
        """
        Tests if the class returns error message for invalid ordered
        entries
        """

        inp = {"Rover 1 Command": "LMLMLMLMM", "Rover 1 State": "1 N 2",
               "Upper-Right Coordinate": "5 5"}

        tst = MarsRover(inp)
        msg = tst.run()[0]

        assert ('Error' in msg and 'Invalid order' in msg)

    def test_invalid_length(self):
        """
        Tests if the class returns error message for invalid number of
        entries
        """

        inp = {"Rover 1 Command": "LMLMLMLMM", "Rover 1 State": "1 2 N N",
               "Upper-Right Coordinate": "5 5"}

        tst = MarsRover(inp)
        msg = tst.run()[0]

        assert ('Error' in msg and 'Invalid number' in msg)

    def test_rover_lost(self):
        """
        Tests if the class returns error message if the rover is lost
        """

        inp = {"Rover 1 Command": "MMMMMMMMMMM", "Rover 1 State": "1 2 N",
               "Upper-Right Coordinate": "5 5"}

        tst = MarsRover(inp)
        msg = tst.run()[0]

        assert ('Error' in msg and 'LOST' in msg)

    def test_rover_clash(self):
        """
        Tests if the class returns error message if rovers clashes
        """

        inp = {"Rover 1 Command": "LMLMLMLMM", "Rover 1 State": "1 2 N",
               "Rover 2 Command": "MM", "Rover 2 State": "1 4 S", "Upper-Right Coordinate": "5 5"}

        tst = MarsRover(inp)
        msg = tst.run()[1]

        assert ('Error' in msg and 'CLASHED' in msg)


