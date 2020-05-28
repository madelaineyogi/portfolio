#Życie jak w Madrycie
print('Cześć!')
print('Jestem tutaj, aby pomóc Ci' \
      + ' w obliczeniu kosztu twoich wymarzonych' \
      + ' wakacji na Majorce!')
name = input('Jeszcze tylko podaj mi swoję imię i możemy zaczynać: ')

print('Okej no to jazda\n' + name)

bilety_lotnicze = int(input("Bilety lotnicze: "))

hotel = int(input("Hotel na Majorce: "))

Zwiedzanie_i_jedzenie = int(input('Koszty jedzenia i zwiedzania: '))

ubezpieczenie = int(input('Ubezpieczenie na w razie wypadku też jest potrzebne: '))
    
total = bilety_lotnicze + hotel + Zwiedzanie_i_jedzenie + ubezpieczenie

if total > 3000:
    print('Słono zapłacisz')
else:
    print('Uf, całkiem tanio!')

print(total ,'PLN')


                   
input('\nAby zakończyć program, naciśnij Enter') 
