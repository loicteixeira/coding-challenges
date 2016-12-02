import os


class LocationDevice:

    ORIENTATIONS = NORTH, EAST, SOUTH, WEST = range(4)
    DIRECTIONS = {'L': -1, 'R': 1}

    def __init__(self):
        self.facing = LocationDevice.NORTH
        self.total_steps = [0] * len(LocationDevice.ORIENTATIONS)

    def rotate(self, direction):
        if direction not in LocationDevice.DIRECTIONS:
            raise RuntimeError('Invalid direction `{}`'.format(direction))

        self.facing += LocationDevice.DIRECTIONS[direction]
        self.facing %= len(LocationDevice.ORIENTATIONS)  # Wrap index so it's always between 0 and size.

    def move_forward(self, distance):
        self.total_steps[self.facing] += distance

    def distance_from_start(self):
        vertical_distance = self.total_steps[LocationDevice.NORTH] - self.total_steps[LocationDevice.SOUTH]
        horizontal_distance = self.total_steps[LocationDevice.EAST] - self.total_steps[LocationDevice.WEST]
        total_distance = abs(vertical_distance) + abs(horizontal_distance)

        return total_distance


def distance(instructions):
    gps = LocationDevice()

    for instruction in instructions.split(', '):
        direction, distance = instruction[0], int(instruction[1:])

        gps.rotate(direction)
        gps.move_forward(distance)

    return gps.distance_from_start()

if __name__ == '__main__':

    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'input.txt')
    with open(file_path, 'r') as f:
        data = f.readline()

    dist = distance(data)
    print('The shortest path to destination is {} block(s) away.'.format(dist))
