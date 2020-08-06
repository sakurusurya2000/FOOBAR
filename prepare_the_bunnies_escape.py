from logging import getLogger
log = getLogger(__name__)

from collections import deque


def answer(maze):
    return search_path(maze, [len(maze) - 1, len(maze[0]) - 1], [0, 0])


def search_path(maze, start, goal):
    queue = deque([(start, 0)])
    weight = {str(start): 1}
    walked_walls = {str(start): 0}
    while queue:
        position, walls = queue.popleft()
        for option, wall in step(maze, position, allow_wall=walls < 1):
            if (
                # First time here
                str(option) not in weight or
                # There is less weight by this new route
                weight[str(option)] > weight[str(position)] + 1 or
                # Same weight but less walls
                (weight[str(option)] == weight[str(position)] + 1 and
                    walked_walls[str(option)] > walls + wall)
            ):
                weight[str(option)] = weight[str(position)] + 1
                walked_walls[str(option)] = walls + wall
                queue.append([option, walls + wall])

    return weight.get(str(goal), 999999999)


def step(maze, position, allow_wall=True):
    """
    Get a list of posible next step

    :rtype: list(tuple(tuple(int), bool))
    :return: list with tuples (next step, there-is-wall)
    """
    directions = [(0, 1), (1, 0), [-1, 0], [0, -1]]
    options = filter(
        lambda x: (
            all([
                # ignore positions that are off the grid
                x[0] >= 0, x[1] >= 0,
                x[0] < len(maze), x[1] < len(maze[0])
            ]) and
            # go through wall
            (maze[x[0]][x[1]] == 0 or allow_wall)
        ),
        # Search all posible directions
        [
            map(sum, zip(position, direction))
            for direction in directions
        ]
    )

    return [
        (option, maze[option[0]][option[1]])
        for option in options
    ]


from logging import basicConfig, DEBUG

basicConfig(level=DEBUG)

maze1 = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0]
]

maze2 = [
    [0, 0, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

maze3 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 1, 1, 1, 1, 1, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

maze4 = [
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]

maze5 = [
    [0, 0],
    [0, 0]
]

maze6 = [
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0]
]
assert answer(maze1) == 7
assert answer(maze2) == 14
assert answer(maze3) == 34
assert answer(maze4) == 11
assert answer(maze5) == 3
assert answer(maze6) == 21
