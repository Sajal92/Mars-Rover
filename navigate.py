class MarsRover:
    """
    Given the initial states(position and orientation) and commands(i.e LMLMLR)
    for the various Mars rovers, this class calculates the final state of all the
    rovers sequentially
    """

    def __init__(self, inp):

        # Input
        self.inp = inp
        self.num_rovers = (len(inp) - 1) // 2
        self.upper_right_corner = inp['Upper-Right Coordinate'].split()
        self.rover_commands = {}
        self.rover_states = {}

        # Command Rules
        self.move_rules = {'W': (-1, 0), 'E': (1, 0), 'N': (0, 1), 'S': (0, -1), "": (0, 0)}
        self.orient_rule_L = {'W': 'S', 'E': 'N', 'N': 'W', 'S': 'E'}
        self.orient_rule_R = {'W': 'N', 'E': 'S', 'N': 'E', 'S': 'W'}

        self.final_states = {}
        self.flag = {'LOST': 0, 'CLASH': 0}

        # Output
        self.msg = []

    def preprocess_input(self):

        """
        Remove spaces and change the input to uppercase
        """

        name_command = ['Rover ' + str(i + 1) + ' Command' for i in range(self.num_rovers)]

        for name in name_command:
            name_state = name.replace("Command", "State")
            self.rover_commands[name] = self.inp[name].upper().replace(" ", "")
            self.rover_states[name_state] = self.inp[name_state].upper().split()

    def check_state(self):

        """
        Check the entries in the input state
        """

        # Entries allowed
        ok = "0123456789NSEW"

        # Loops over each rover state and check for missing or invalid entries
        for k, s in self.rover_states.items():
            if len(s) == 0:
                self.msg.append("Error: Missing entries for " + k)

            elif len(s) != 0 and len(s) != 3:
                self.msg.append("Error: Invalid number of entries in " + k)

            elif not all(c in ok for c in ''.join(s)):
                self.msg.append("Error: Invalid entries in " + k)

            elif not (all(c in ok for c in ''.join(s[0] + s[1])) and s[2] in 'NSWE'):
                self.msg.append("Error: Invalid order of entries in " + k)

            elif len(s[2]) != 1:
                self.msg.append("Error: Invalid entries in orientation for " + k)

    def check_command(self):

        """
        Check the entries in the input command
        """
        # Entries allowed
        ok = "LRM"

        # Loops over each rover command and check for invalid entries
        for k, s in self.rover_commands.items():
            if not all(c in ok for c in s):
                self.msg.append("Error: Invalid entries in " + k)

    def check_plateau_corner(self):

        """
        Check the entries in the input plateau upper-right coordinates
        """

        # Entries allowed
        ok = "0123456789"
        s = self.upper_right_corner

        if len(s) == 0:
            self.msg.append("Error: Missing entries for plateau upper-right coordinates")

        elif len(s) != 0 and len(s) != 2:
            self.msg.append("Error: Invalid number of entries in plateau upper-right coordinates")

        elif not all(c in ok for c in ''.join(s)):
            self.msg.append("Error: Invalid entries in plateau upper-right coordinates")

    def check_if_lost(self, state):

        """
        Check if any rover is lost i.e fall of the plateau
        """
        # Current coordinates of rover
        x = int(state[0])
        y = int(state[1])

        # Plateau upper-right corner coordinates
        x_plateau = int(self.upper_right_corner[0])
        y_plateau = int(self.upper_right_corner[1])

        if x < 0 or y < 0 or x > x_plateau or y > y_plateau:
            self.flag['LOST'] = 1

    def check_clash(self, state):

        """
        Check if any rover clashes with other rovers during navigation
        """

        # Checks if the position of current rover clashes with
        # the position of previous rovers
        if ''.join(state[0:2]) in self.final_states:
            self.flag['CLASH'] = 1

    def next_state(self, state, c):
        """
        Returns the next state to the current state based on the command c
        """

        if c == 'L':
            state[2] = self.orient_rule_L[state[2]]
        elif c == 'R':
            state[2] = self.orient_rule_R[state[2]]
        else:
            state[0] = str((int(state[0]) + self.move_rules[state[2]][0]))
            state[1] = str((int(state[1]) + self.move_rules[state[2]][1]))

        return state

    def final_state(self, state, command):

        """
        Returns the final state of the rover based on the initial state
        and the command given. Also, checks if the rover is lost or clashes
        with any other rover in between
        """

        for c in command:
            self.check_if_lost(state)
            self.check_clash(state)
            state = self.next_state(state, c)

        return state

    def run(self):

        """
        Navigate the rover based on the inputs
        """

        # Preprocess all the inputs
        self.preprocess_input()

        # Check entries inside the inputs
        self.check_state()
        self.check_command()
        self.check_plateau_corner()

        # Returns error message if check entries failed
        if self.msg:
            return self.msg

        # Iterate through each rover sequentially
        for k in self.rover_commands.keys():

            # Key to get particular rover's state
            newKey = k.replace("Command", "State")

            # Returns final state based on the command
            state = self.final_state(self.rover_states[newKey], self.rover_commands[k])

            # Checks if rover lost and returns an error message
            if self.flag['LOST'] == 1:
                self.msg.append('Error: ' + k.replace("Command", "") + 'LOST')
                print('msg: ', self.msg)
                return self.msg

            # Checks if rover clashed into other rover and returns an error message
            if self.flag['CLASH'] == 1:
                self.msg.append('Error: ' + k.replace("Command", "") + 'CLASHED into other rover')
                return self.msg

            # If no error the update the rover's final state
            self.rover_states[newKey] = state
            self.final_states[''.join(state[0:2])] = 1

            # Output for the final states of all the rovers
            self.msg.append(k.replace("Command", "") + "final state: " + ' '.join(state) + ' ')

        return self.msg
