def pde_contour_class(p, first_x, last_x, first_y, last_y):  # p = point
    if p[1] == first_y:
        return 'bottom'
    elif p[1] == last_y:
        return 'top'
    elif p[0] == first_x:
        return 'left'
    elif p[0] == last_x:
        return 'right'
    else:
        return None

# Returns a function in contour:


def pde_contour_func(clazz):
    if clazz == 'bottom':
        return 10
    elif clazz == 'top':
        return 100
    elif clazz == 'left':
        return 0
    elif clazz == 'right':
        return 0

# Returns a function in domain:


def pde_domain_func(p):
    return 0
