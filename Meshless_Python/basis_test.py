import basis as b
import basismatrix as bm

# Pde_Basis:

pde1 = b.pde_basis(1)[0]
pde1_x = b.pde_basis(1)[1]
pde1_y = b.pde_basis(1)[2]
pde1_xx = b.pde_basis(1)[3]
pde1_yy = b.pde_basis(1)[4]
pde1_xy = b.pde_basis(1)[5]

pde2 = b.pde_basis(2)[0]
pde2_x = b.pde_basis(2)[1]
pde2_y = b.pde_basis(2)[2]
pde2_xx = b.pde_basis(2)[3]
pde2_yy = b.pde_basis(2)[4]
pde2_xy = b.pde_basis(2)[5]

pde3 = b.pde_basis(3)[0]
pde3_x = b.pde_basis(3)[1]
pde3_y = b.pde_basis(3)[2]
pde3_xx = b.pde_basis(3)[3]
pde3_yy = b.pde_basis(3)[4]
pde3_xy = b.pde_basis(3)[5]

# Pde_data:

data_test = [[0, 0], [4, 2.0], [4, 4]]

# Pde_linear_basis:


def test_linear_basis():
    assert bm.create_basis(pde1, data_test) == [[1, 0, 0], [1, 4, 2], [1, 4, 4]]


def test_linear_basis_x():
    assert bm.create_basis(pde1_x, data_test) == [[0, 1, 0], [0, 1, 0], [0, 1, 0]]


def test_linear_basis_y():
    assert bm.create_basis(pde1_y, data_test) == [[0, 0, 1], [0, 0, 1], [0, 0, 1]]


def test_linear_basis_xx():
    assert bm.create_basis(pde1_xx, data_test) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_linear_basis_yy():
    assert bm.create_basis(pde1_yy, data_test) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_linear_basis_xy():
    assert bm.create_basis(pde1_xy, data_test) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# Pde_quadratic_basis test:


def test_quadratic_basis():
    assert bm.create_basis(pde2, data_test) == [[1, 0, 0, 0, 0, 0], [1, 4, 16, 2.0, 4.0, 8.0], [1, 4, 16, 4, 16, 16]]


def test_quadratic_basis_x():
    assert bm.create_basis(pde2_x, data_test) == [[0, 1, 0, 0, 0, 0], [0, 1, 8, 0, 0, 2], [0, 1, 8, 0, 0, 4]]


def test_quadratic_basis_y():
    assert bm.create_basis(pde2_y, data_test) == [[0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 4, 4], [0, 0, 0, 1, 8, 4]]


def test_quadratic_basis_xx():
    assert bm.create_basis(pde2_xx, data_test) == [[0, 0, 2, 0, 0, 0], [0, 0, 2, 0, 0, 0], [0, 0, 2, 0, 0, 0]]


def test_quadratic_basis_yy():
    assert bm.create_basis(pde2_yy, data_test) == [[0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 2, 0]]


def test_quadratic_basis_xy():
    assert bm.create_basis(pde2_xy, data_test) == [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1]]


# Pde_cubic_basis test:


def test_cubic_basis():
    assert bm.create_basis(pde3, data_test) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 4, 2, 16, 8, 4, 64, 32, 16, 8],
                                                [1, 4, 4, 16, 16, 16, 64, 64, 64, 64]]


def test_cubic_basis_x():
    assert bm.create_basis(pde3_x, data_test) == [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 8, 2, 0, 48, 16, 4, 0],
                                                  [0, 1, 0, 8, 4, 0, 48, 32, 16, 0]]


def test_cubic_basis_y():
    assert bm.create_basis(pde3_y, data_test) == [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 4, 4, 0, 16, 16, 12],
                                                  [0, 0, 1, 0, 4, 8, 0, 16, 32, 48]]


def test_cubic_basis_xx():
    assert bm.create_basis(pde3_xx, data_test) == [[0, 0, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0, 24, 4, 0, 0],
                                                   [0, 0, 0, 2, 0, 0, 24, 8, 0, 0]]


def test_cubic_basis_yy():
    assert bm.create_basis(pde3_yy, data_test) == [[0, 0, 0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0, 0, 8, 12],
                                                   [0, 0, 0, 0, 0, 2, 0, 0, 8, 24]]


def test_cubic_basis_xy():
    assert bm.create_basis(pde3_xy, data_test) == [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 8, 4, 0],
                                                   [0, 0, 0, 0, 1, 0, 0, 8, 8, 0]]
