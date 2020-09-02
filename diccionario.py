def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        ingles=input("dame el valor en ingles")
        español=input("dame el valor en español")
        diccionario[ingles]=español
        continua=input("desea continuar s/n")
    return diccionario

def imprimir(diccionario):
    
    for ingles in diccionario:
        print(ingles,diccionario[ingles])


def acceder (diccionario):
    busc=input("que palabra va a buscar")
    ent="S"
    if busc in diccionario:
        print("la palabra significa",diccionario[busc])

    else:
         print("la palabra no existe")
    
    ent=input("desea repetir s/n")
    if ent=="s":
        acceder(diccionario)



diccionario=cargar()
imprimir(diccionario)
acceder(diccionario)


