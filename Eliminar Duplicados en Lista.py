"""
Funcion que sirve para eliminar los valores duplicados dentro de una lista dada
"""

def eliminarduplicados(lista):
    list_fixed = []
    for number in lista:
        if number in list_fixed:
            continue
        else:
            list_fixed.append(number)
    list_fixed.sort()
    return list_fixed

"""
Ejemplo de lista a eliminar duplicados
"""

lista_con_duplicados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   

"""
Aplicando la funcion
"""

lista_nueva = eliminarduplicados(lista_con_duplicados)

print(lista_nueva)

