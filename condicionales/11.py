import os 
os.system("cls")

numero = int( input("Número : ") )

#if numero > 0 : print ("Positivo")
#elif numero == 0 : print ( "Cero" )
#else : print( "Negativo" )

print( "Positivo" if numero > 0 else "Negativo" if numero else "Cero")
