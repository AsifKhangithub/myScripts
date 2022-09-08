#!/usr/bin/python3/

#range max tal att prova
numbersTotest = input ('Hur många tal vill du undersöka?: ')

#yttre loop - prova samtliga tal upp till numbersTotest
for i in range(1, numbersTotest+1):
   #innreloop - prova om talet är jämförtbar med något annat tal än '1' och 'i'
   #if är det ej ett primtal 
   for k in range(2,numbersTotest):
      if i % k == 0
         print(f'{i}ej ett primtal') 
	 break
