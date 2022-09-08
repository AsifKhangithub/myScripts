#!/usr/bin/python3

#fråga användare om hunden är hungrig
svar = input('är hund hungrig?')

'''
#skriva ut maten hunden om svar 'ja' skriv ut 'Hunden mätt' om svar 'nej'
#annars, skriv ut 'förstår ej svar'
'''

if svar.lower() == 'ja':
   print(f' du svarade {svar} - mata hunden')

elif svar.lower() == 'nej':
   print(f' du svarade {svar} - hunden mätt')
else:
   print('Förstår ej svar')

print('***slut på program**')




