
def interpol_basis(basis_order):  # Defines basis configuration of interpolation.
    if basis_order == 1:  # Linear Basis
        interpol_polynomial_basis = ["1", "x", "y"]
    elif basis_order == 2:  # Quadratic Basis
        interpol_polynomial_basis = ["1", "x", "x**2", "y", "y**2", "x*y"]
    elif basis_order == 3:  # Cubic Basis
        interpol_polynomial_basis = ["1", "x", "y", "x**2", "x*y", "y**2", "x**3", "(x**2)*y", "x*(y**2)", "y**3"]

    return interpol_polynomial_basis


def pde_basis(basis_order):  # Defines basis configuration of pde.
    if basis_order == 1:  # Linear Basis
        polynomial_basis = ["1", "x", "y"]
        polynomial_basis_x = ["0", "1", "0"]  # First derivative in x
        polynomial_basis_y = ["0", "0", "1"]
        polynomial_basis_xx = ["0", "0", "0"]  # Second derivative in x
        polynomial_basis_yy = ["0", "0", "0"]
        polynomial_basis_xy = ["0", "0", "0"]
    elif basis_order == 2:  # Quadratic Basis
        polynomial_basis = ["1", "x", "x**2", "y", "y**2", "x*y"]
        polynomial_basis_x = ["0", "1", "2*x", "0", "0", "y"]
        polynomial_basis_y = ["0", "0", "0", "1", "2*y", "x"]
        polynomial_basis_xx = ["0", "0", "2", "0", "0", "0"]
        polynomial_basis_yy = ["0", "0", "0", "0", "2", "0"]
        polynomial_basis_xy = ["0", "0", "0", "0", "0", "1"]
    elif basis_order == 3:  # Cubic Basis
        polynomial_basis = ["1", "x", "y", "x**2", "x*y", "y**2", "x**3", "(x**2)*y", "x*(y**2)", "y**3"]
        polynomial_basis_x = ["0", "1", "0", "2*x", "y", "0", "3*(x**2)", "2*x*y", "(y**2)", "0"]
        polynomial_basis_y = ["0", "0", "1", "0", "x", "2*y", "0", "(x**2)", "2*x*y", "3*(y**2)"]
        polynomial_basis_xx = ["0", "0", "0", "2", "0", "0", "6*x", "2*y", "0", "0"]
        polynomial_basis_yy = ["0", "0", "0", "0", "0", "2", "0", "0", "2*x", "6*y"]
        polynomial_basis_xy = ["0", "0", "0", "0", "1", "0", "0", "2*x", "2*y", "0"]

    else:
        input('Pde order: ')

    pdebasis = [polynomial_basis, polynomial_basis_x, polynomial_basis_y, polynomial_basis_xx, polynomial_basis_yy,
                 polynomial_basis_xy]
    return pdebasis
