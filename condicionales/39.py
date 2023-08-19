import os
os.system("cls")

bHorasAusencia = float( input("Horas Ausencia : ") ) <= 1.5
bTDefectuosos = int( input("Tornillos Defectuosos : ") ) < 300
bTBuenos = int( input("Tornillos Buenos : ") ) > 10000

if not bHorasAusencia and not bTDefectuosos and not bTBuenos : grado = 5 
if not bHorasAusencia and not bTDefectuosos and not bTBuenos : grado = 6