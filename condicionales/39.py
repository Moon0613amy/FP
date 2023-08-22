import os
os.system("cls")

bHorasAusencia = float( input("Horas Ausencia : ") ) <= 1.5
bTDefectuosos = int( input("Tornillos Defectuosos : ") ) < 300
bTBuenos = int( input("Tornillos Buenos : ") ) > 10000

if not bHorasAusencia and not bTDefectuosos and not bTBuenos : grado = 5 
elif bHorasAusencia and not bTDefectuosos and not bTBuenos : grado = 7
elif not bHorasAusencia and bTDefectuosos and not bTBuenos : grado = 8
elif not bHorasAusencia and not bTDefectuosos and bTBuenos : grado = 9
elif bHorasAusencia and bTDefectuosos and not bTBuenos : grado = 12
elif bHorasAusencia and not bTDefectuosos and bTBuenos : grado = 13
elif not bHorasAusencia and bTDefectuosos and bTBuenos : grado = 15
elif bHorasAusencia and bTDefectuosos and bTBuenos : grado = 20

print(f"Grado : {grado}")