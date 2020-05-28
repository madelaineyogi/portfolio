print('witaj na koncercie Ariany Grande!')
print('Wydaję mi się, że ostatnie bilety już się sprzedały. Przykro mi')

kasa = int(input('Ile jesteś w stanie zapłacić za ten bilet?'))

if kasa > 200:
    print('Oh znalazłam ostatni!')
    zdanie = ('Dziś jest twój szczęśliwy dzień')         
    print(zdanie.upper())
else:
    print('Przykro mi, chyba musisz wórcić do domu!')



input('\n\nAby zakończyć naciśnij Enter')
