# Implementación de un DFA usando tablas

# Función para reconocer si el string es reconocido por el DFA
def reconocetabla(tabla, w):
    dic = {'0': 0, '1':1} # A es la primera columna, B es la segunda
    estado = 0

    for caracter in w:
        if caracter in "01$":
            if caracter == '$':
                if estado == 0:
                    return True
                else: 
                    return False
            else:
                estado = tabla [estado][dic[caracter]]
        else: 
            return False

tabla = [[1,2],[0,3],[3,0],[2,1]]
w = '0011$'

print(reconocetabla(tabla, w))