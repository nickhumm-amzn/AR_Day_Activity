import math

# Also known as the L1 norm, the manhattan distance is the distance between two points measured along axes at right angles
def manhattan_dist_2D(coord_pair_1, coord_pair_2):
    if not all(isinstance(val, int) for val in coord_pair_1 + coord_pair_2):
        raise Exception('Coordinates passed to Utils.manhattan_dist_2D were not all of type: int')
    if len(coord_pair_1) < 2 or len(coord_pair_2) < 2:
        raise Exception('Coordinates passed to Utils.manhattan_dist_2D did not have at least 2 values in each argument')

    return abs(coord_pair_1[0] - coord_pair_2[0]) + abs(coord_pair_1[1] - coord_pair_2[1])

# Also known as the L1 norm, the manhattan distance is the distance between two points measured along axes at right angles
def euclidean_dist_2D(coord_pair_1, coord_pair_2):
    if not all(isinstance(val, int) for val in coord_pair_1 + coord_pair_2):
        raise Exception('Coordinates passed to Utils.euclidean_dist_2D were not all of type: int')
    if len(coord_pair_1) < 2 or len(coord_pair_2) < 2:
        raise Exception('Coordinates passed to Utils.euclidean_dist_2D did not have at least 2 values in each argument')

    return math.dist(coord_pair_1, coord_pair_2[0])