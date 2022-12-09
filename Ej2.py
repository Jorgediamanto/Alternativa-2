
def expand(expression):
    # Extraer a, b y n de la expresión
    a, b, n = extract_values_from_expression(expression)
    # Inicializar la cadena resultante como una cadena vacía
    result = ""
    # Iterar sobre las potencias de x en el resultado expandido
    for i in range(n, -1, -1):
        # Calcular el coeficiente para el término actual
        coefficient = n * (n - 1) * ... * (n - i + 1) / i!
        # Añadir el término al resultado
        result += format_term(coefficient, a, i, b)
    return result

def expand(expression):
   # Extraer a, b y n de la expresión
   a, b, n = extract_values_from_expression(expression)

   # Inicializar la cadena resultante como una cad

def decrypt(ciphertext, key):
   # Crear una cuadrícula con tantas filas como la clave y tantas columnas como la longitud del texto cifrado
   grid = create_grid(ciphertext, key)

   # Colocar la primera letra del texto cifrado en la esquina superior izquierda de la cuadrícula
   grid[0][0] = ciphertext[0]

   # Inicializar la posición actual en la cuadrícula como (0, 0)
   current_position = (0, 0)

   # Iterar sobre las letras del texto cifrado
   for letter in ciphertext[1:]:
       # Avanzar en diagonal hacia abajo en la cuadrícula
       current_position = move_down(current_position, grid)

       # Colocar la letra actual en la posición actual en la cuadrícula
       grid[current_position[0]][current_position[1]] = letter

   # Atravesar la cuadrícula en zig-zag y leer las letras en orden
   plaintext = traverse_grid(grid)

   # Reemplazar los nulos con espacios en blanco
   plaintext = plaintext.replace("X", " ")

   return plaintext


def expand(expression):
    # Extraer a, b y n de la expresión
    a, b, n = extract_values_from_expression(expression)
    # Inicializar la cadena resultante como una cadena vacía
    result = ""
    # Iterar sobre las potencias de x en el resultado expandido
    for i in range(n, -1, -1):
        # Calcular el coeficiente para el término actual
        coefficient = n * (n - 1) * ... * (n - i + 1) / i!
        # Añadir el término al resultado
        result += format_term(coefficient, a, i, b)
    return result

def expand(expression):
   # Extraer a, b y n de la expresión
   a, b, n = extract_values_from_expression(expression)

   # Inicializar la cadena resultante como una cad