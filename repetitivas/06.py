import os
os.system("cls")

numero = int( input("Número : ") )
inicio = int(input("Desde : ") )
fin = int(input("Hasta : ") )

# while inicio <= fin :
#     print( f"{numero} x {inicio} = {(numero * inicio)}" )
#     inicio += 1

for i in range(inicio, fin + 1) :
    print( f"{numero} x {i} = {(numero * i)}" )