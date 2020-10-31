from itertools import product

def move(state, x):
    if x == 'D':
        state[1] -= 0
    elif x == 'U':
        state[1] += 1
    elif x == 'L':
        state[0] -= 1
    elif x == 'R':
        state[0] += 1
    return tuple(state)


aw = {'D': 'U',
      'U': 'D',
      'L': 'R',
      'R': 'L',}

def f(m):
    return aw[m]

def asymmetric_walk(L):
    return tuple(map(f, L))


if __name__ == "__main__":
    k = 11
    steps = list(product(['L', 'R', 'U', 'D'], repeat=k))
    filtered_steps = set(steps)
    # filter all symmetric walks
    # print(filtered_steps)
    for step in steps:
        if step in filtered_steps:
            o = asymmetric_walk(step)
            filtered_steps.discard(o)
            # print(o in filtered_steps)
            # print(step, o)
    coordinates = []
    for walk in filtered_steps:
        coordinate = [(0, 0)]
        for i, direction in enumerate(walk):
            state = list(coordinate[i])
            coordinate.append(move(state, direction))
        coordinates.append(coordinate)
    d = [x for x in coordinates if len(set(x)) == k+1]
