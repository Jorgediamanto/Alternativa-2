import math

def contar_num_posibilidades(longitud):
    x = 9-longitud
    numero_variaciones = math.factorial(9)/math.factorial(x)
    return numero_variaciones



f=contar_num_posibilidades(4)
print(f)