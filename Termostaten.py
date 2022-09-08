#läs user-input

#Evluera
nuTemp = int(input('Hur många grader är det idag?'))


'''
# Slå på om temperature  '<25' skriv ut 'temperature är' om svar '>24'
#annars, skriv ut 'Invalid'
'''

if nuTemp < 25:
   print(' slå på värme')

elif nuTemp > 24:
   print(' stäng av värme')
else:
   print('invalid')

print('***slut på program**')
