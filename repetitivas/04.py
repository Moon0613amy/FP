import os
os.system("cls")

numero = int( input("Numero : ") )
multiplos = int( input(" # multiplos : ") )

rpta = ""
for i in range(1, multiplos + 1) :
    rpta += str(numero * i) + ( ", " if i < multiplos else "" )

print( f"Los multiplos de {numero} = {rpta}" )    