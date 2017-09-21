# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    second_coords = []
    for point in segments:
        second_coords.append(point[1])
    points.append(min(second_coords)) 
    sorted_segments = [s for _,s in sorted(zip(second_coords,segments))]

    for point in sorted_segments:
        if point[0] <= points[-1] <= point[1]:
            continue
        else:
            points.append(point[1])
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
