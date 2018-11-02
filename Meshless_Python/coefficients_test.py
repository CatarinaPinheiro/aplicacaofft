import coefficients as c
import basis as b
import numpy as np

pde_differential_x = {  # Information about pde equation
    'order': 1,  # order of pde
    'var': 'x',  # Variable
    'base1': b.pde_basis(1)[1],
    'base2': b.pde_basis(1)[3]
}

pde_differential_xx = {  # Information about pde equation
    'order': 2,  # order of pde
    'var': 'x',  # Variable
    'base1': b.pde_basis(1)[1],
    'base2': b.pde_basis(1)[3]
}

r_data = [[0, 1], [0.5, 1.5], [1, 2], [1.5, 2.5], [2, 3], [2.5, 3.5], [3, 4], [3.5, 4.5], [4, 5]]
contour_point = [[0, 0], [4, 4]]


def test_coefficients():
    a = c.coefficients(r_data, r_data[4], 1, contour_point)
    d = [[0, 0, 0, 0.28124297, 0.375, 0.28124297, 0, 0, 0]]
    assert np.allclose(a, d)


def test_coefficients_first_derivative():
    a = c.coefficients(r_data, r_data[4], 1, contour_point, pde_differential_x)
    d = [[0, 0, 0.3749625, -2.24996719, -0.125, 2.12496719, -0.3749625, 0, 0]]
    assert np.allclose(a, d)


def test_coefficients_second_derivative():
    a = c.coefficients(r_data, r_data[4], 1, contour_point, pde_differential_xx)
    d = [[0, 0, - 13.49938753, 5.04672344, 10.3749625, 3.68734844, - 13.12438753, 0, 0]]
    assert np.allclose(a, d)
