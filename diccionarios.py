#Algoritmo que imprima de manera ascendente los valores (todos del mismo tipo de un diccionario)

def asc_diccionario(diccionario):
    numeros=sorted(diccionario.keys())
    dic_ordenado={}
    for numero in numeros:
        dic_ordenado[numero]=diccionario[numero]
        
    return dic_ordenado

numeros={5:'c',2:'f',3:'s',1:'l'}
segundo={6:'h',41:'5',5:'j'}

print(asc_diccionario(numeros))

#Algoritmo que verifique si todas las clave:valor de un diccionario se encuentran en otro

def comparar(diccionario1, diccionario2):
    for key, item in diccionario1.items():
        if key not in diccionario2 or diccionario2[key] != item:
            return False
    return True
        
#print(comparar(numeros, segundo))

#Mezclar dos diccionarios
def mezclar_dicc(diccionario1,diccionario2):
    diccionario1.update(diccionario2)
    return diccionario1

#print(mezclar_dicc(numeros, segundo ))

#Dada una lista con nombre, apellido, edad, imprimiva rango de edades 
def nombres(diccionario,min,max):
    for key,item in diccionario.items():
        if item['edad']in range(min,max):
            print(key, item['apellido'])

personas = {
    'Juan': {'nombre':'Juan', 'apellido': 'Pérez', 'edad': 25},
    'Ana': {'nombre':'Ana', 'apellido': 'Pérez', 'edad': 32},
    'Luis': {'nombre':'Luis', 'apellido': 'Pérez', 'edad': 21}
}

#nombres(personas, 20, 30)