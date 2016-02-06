
def encuentra_palabra(archivo, n_letras=4):
    """
    Encuentra la palabra que mas se repite en 'archivo'
    que tiene al menos 'n_letras'.
    """
    filein = open(archivo, "r")
    texto = filein.readlines()

    cuenta = {}
    #print "Hay {} lineas en el texto".format(n_lines)
    for linea_completa in texto:
        linea = linea_completa.split()
        for palabra in linea:
            if(len(palabra)>=n_letras):
                if cuenta.has_key(palabra):
                    cuenta[palabra] += 1
                else:
                    cuenta[palabra] = 1
    return  max(cuenta, key=cuenta.get), cuenta

p, cuenta = encuentra_palabra("hamlet.txt")
print "La palabra mas repetida es: {} que se encuentra {} veces\n".format(p, cuenta[p])

p, cuenta = encuentra_palabra("hamlet.txt", n_letras = 8)
print "La palabra mas repetida es: {} que se encuentra {} veces\n".format(p, cuenta[p])
