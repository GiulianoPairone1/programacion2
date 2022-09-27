#Definir una función listaPares  que reciba una lista con numeros y devuelva  una lista con los números pares. (2,5 puntos)
def listapares(listnumeros):
    listpares=[]
    for i in listnumeros:
        if(i %2  == 0):
            listpares.append(i)
    return listpares

lista1=[1,2,3,4,5,6,7,8,9,]
print(listapares(lista1))