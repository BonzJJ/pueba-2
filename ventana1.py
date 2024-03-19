def ordenarBurbuja(lista):
   #lista = [50, 51, 55, 53, 57, 52, 54]
    ultimaposicion = len(lista) - 1

    for pos1 in range(ultimaposicion, 0 , -1):
        for pos2 in range(pos1):
            if lista[pos2] > lista[pos2+1]:
                lista[pos2],lista[pos2+1] = lista[pos2+1], lista[pos2]
    return(lista)

def busquedaSecuencial(lista, numero):
    pos = 0
    existe = False
    while pos < len(lista) and not existe:
        if lista[pos] == numero:
            existe = True
        else:
            pos += 1
    return existe

def busquedaBinaria(lista, numero):
    indice1 = 0
    indiceUltimo = len(lista) - 1

    existe = False

    while indice1 <= indiceUltimo and not existe:
        mitad = (indice1 + indiceUltimo) // 2
        if lista[mitad] == numero:
            existe = True
        else:
            if numero < lista[mitad]:
                indiceUltimo = mitad - 1
            else:
                indice1 = mitad + 1
    return existe

if __name__ == '__main__':
    lista = [50,51,55,53,57,52,54]
    #l = ordenarBurbuja(lista)
    #print(l)

    numero = 51

    print(lista)
    ordenarBurbuja(lista)
    print(lista)
    print('BÚSQUEDA SECUENCIAL : ¿Existe el número?: '+ str(numero)+' '+ str(busquedaSecuencial(lista , numero)))

    print('BÚSQUEDA BINARIA : ¿Existe el número?: '+ str(numero)+' '+ str(busquedaBinaria(lista, numero)))





