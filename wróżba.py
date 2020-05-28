#ciasteczko z wróżbą
#program generuję wróżbę

wrozba1 = 'jakie piękne oczy!'
wrozba2 = 'niezły masz cios!'
wrozba3 = 'ratunku!'
wrozba4 = 'spójrz w górę!'
wrozba5 = 'kto jak nie ty?'

print('witaj w programie wróżb!')
print('Mam nadzieję, że Ci się spodoba')

liczba = int(input('Wybierz liczbę od 1 do 5 '))

if liczba == 1:
    print(wrozba1)
elif liczba == 2:
    print(wrozba2)
elif liczba == 3:
    print(wrozba3)
elif liczba == 4:
    print(wrozba4)
elif liczba == 5:
    print(wrozba5)
else:
    print('Miała być liczba od 1 do 5!')
    
input('\nAby zakończyć naciśnij Enter')
