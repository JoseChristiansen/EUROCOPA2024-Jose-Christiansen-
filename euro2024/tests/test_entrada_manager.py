

mi_variable_global = 10


def modificar_variable():

    global mi_variable_global

    mi_variable_global = 20


print(mi_variable_global)  # Imprime 10

modificar_variable()

print(mi_variable_global)  # Imprime 20