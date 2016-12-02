import os

from no_time_for_a_taxicab_part1 import LocationDevice as BaseLocationDevice


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)


class Segment:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x

    def intersection(self, other):
        # Flip segments around so we always deal with horizontal and vertical in the same order.
        if self.is_horizontal() and other.is_vertical():
            h, v = self, other
        elif self.is_vertical() and other.is_horizontal():
            h, v = other, self

        # Because it uses Taxicab geometry, we only care of horizontal and vertical segments.
        else:
            raise NotImplementedError()

        intersects_horizontally = v.start.y <= h.start.y <= v.end.y
        intersects_vertically = h.start.x <= v.start.x <= h.end.x

        if not(intersects_horizontally and intersects_vertically):
            return

        intersection = Point(v.start.x, h.start.y)
        return intersection

    def __str__(self):
        return '{start} to {end}'.format(start=self.start, end=self.end)


class LocationDevice(BaseLocationDevice):

    @property
    def current_position(self):
        x = self.total_steps[LocationDevice.EAST] - self.total_steps[LocationDevice.WEST]
        y = self.total_steps[LocationDevice.NORTH] - self.total_steps[LocationDevice.SOUTH]

        return Point(x, y)


def distance_to_first_intersection(instructions):
    gps = LocationDevice()
    segments = []

    for instruction in instructions.split(', '):
        start_position = gps.current_position

        direction, distance = instruction[0], int(instruction[1:])
        gps.rotate(direction)
        gps.move_forward(distance)

        end_position = gps.current_position
        new_segment = Segment(start_position, end_position)

        # Since we always turn left or right, previous segments are in turn parrallel or perpendicular.
        # Starting at 0 or 1 with a step of 2 only returns perpendicular segments.
        # Lastly, there is no point checking for intersection with the previous segment
        # since they won't intersect (start of new segment is end of previous segment), using end of -1.
        start_index = (len(segments) + 1) % 2
        perpendicular_segments = segments[start_index:-1:2]

        for segment in perpendicular_segments:
            intersection = new_segment.intersection(segment)
            if intersection:
                distance_to_intersection = abs(intersection.x) + abs(intersection.y)
                return distance_to_intersection

        segments.append(new_segment)


if __name__ == '__main__':

    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'input.txt')
    with open(file_path, 'r') as f:
        data = f.readline()

    dist = distance_to_first_intersection(data)
    if dist:
        print('The first intersection is {} block(s) away.'.format(dist))
    else:
        print('There is no intersection :(')
