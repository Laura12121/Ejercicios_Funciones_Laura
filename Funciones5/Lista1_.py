#funciones
def elementos(numero,cadena,ordenar):
    print('contenido de la lista\n')
    for i in numero:
        print(f'{i}')
    print(f'\ncadena de caracter\n{cadena}')
    print(f'\nordenar\n{ordenar}')
numero=['uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez']
cadena=",".join(numero)
ordenar=sorted(numero)
elementos(numero,cadena,ordenar)
def encontrar(longitud):
    for i in numero:
        buscar=input('\nbuscar el numero para salir(s):  ')
        if buscar in numero:
            print(f'{buscar}')
        else:
            print('numero no existente')
        if buscar=='s':
            print(':o')
            break
        print(f'\nlongitud : {longitud}')
longitud=len(numero)
encontrar(longitud)



