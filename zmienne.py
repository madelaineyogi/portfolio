'''days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'san']

workdays = days.copy()
workdays.remove('sat')
workdays.remove('san')

print('days: ', days)
print('workdays: ', workdays)


a = ()#krotka
b = []#lista
c = {}#słownik
print(type(a), type(b), type(c))

listOfColors = ["red", "orange", "green", "violet", "blue", "yellow"]

def get_list_of_colors(listOfColors, n):
    return listOfColors[:n]

for i in range (1,len(listOfColors)+1):
    print(get_list_of_colors(listOfColors, i))
'''
'''
print('Wprowdz kwotę ogólną rachunku')

rachunek = int(input())
napiwek15 = (rachunek * 0.15)
napiwek20 = (rachunek * 0.20)

wynik1 = print('Kwota napiwku 15% ', napiwek15, 'PLN')
wynik2 = print('Kwota napiwku 20% ', napiwek20, 'PLN')

print(type(wynik1))
print(type(wynik2))    
'''
