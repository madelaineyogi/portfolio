'''
#zad 11 (6)

print('podaj trzy liczby oraz napis')

liczba1 = int(input('pierwsza liczba __'))
liczba2 = int(input('druga liczba __'))
liczba3 = int(input('trzecia liczba __'))
napis = input('napis __')

len(napis)
print(napis)
    
print(napis[liczba1:liczba1+1],napis[liczba2:liczba2+1],napis[liczba3:liczba3+1])

#zad 10 (6)

print('podaj trzy napisy')

napis1 = input('napis ...')
napis2 = input('napis ...')
napis3 = input('napis ...')

nowynapis1 = napis1[::-1]
nowynapis2 = napis2[::-1]
nowynapis3 = napis3[::-1]

if nowynapis1 < nowynapis2 and nowynapis2 < nowynapis3:
    print('napisy są ustawione w kolejności rosnącej')
else:
    print('napisy są ustawione w kolejności malejącej')


#zad 9 (6)
print('podaj dwa napisy')

napis1 = input('napis ...')
napis2 = input('napis ...')

if napis1 < napis2:
    print(napis1,napis2)
else:
    print(napis2,napis1)

#zad 8 (6)


print('podaj dwa napisy oraz liczbę')

napis1 = input('napis ...')
napis2 = input('napis ...')
liczba = int(input())

nowynapis = print(napis1[::liczba],napis2[::liczba])

'''























