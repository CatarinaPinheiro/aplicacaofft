import minimumradius as mr

r_data = [[0, 0], [0.5, 0.5], [1, 1], [1.5, 1.5], [2, 2], [2.5, 2.5], [3, 3], [3.5, 3.5], [4, 4]]
contour_point = [[0, 0], [4, 4]]


def test_radius():
    assert (mr.get_radius(r_data, r_data[4], 4, contour_point) - 1.41421356237) <= 0.0000001


def test_radius_contour():
    assert (mr.get_radius(r_data, r_data[1], 2, contour_point) - 1.41421356237) <= 0.0000001
