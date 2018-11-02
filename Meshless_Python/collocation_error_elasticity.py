import error as e
import application_elasticity as ae

displacement_y = []
for i in range(len(ae.answer)):
    if (i % 2) != 0 and i != 0:
        displacement_y.append(ae.answer[i])

xs = [x for x, y in ae.pde_data]
ys = [y for x, y in ae.pde_data]


def analytical_function(y):
    return -y / 4


analytical = [analytical_function(y) for x, y in ae.pde_data]
print('Valor de y: ', list(y for [x, y] in ae.pde_data))

collocation_error = e.absolute_error(analytical, displacement_y)
print('Analitico:', analytical)
print('Aproximado: ', displacement_y)
print(collocation_error)
print(max(collocation_error))
