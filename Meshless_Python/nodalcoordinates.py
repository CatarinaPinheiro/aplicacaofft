# Set up nodal coordinates (Segments number)


def segments(first, last, count):
    step = float(last - first) / count
    return [first + i * step for i in range(count + 1)]


# returns array except it's first and last elements.

def inside(a):
    return [a[i + 1] for i in range(len(a) - 2)]


# Returns Cartesian Product of two sets.
def cartesianproduct(a, b):
    return [[x, y] for x in a for y in b]
