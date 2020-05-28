#skrypt, który prosi użytkownika o pobranie dwóch liczb i jeżli jedna dzieli się przez drugą wyświetli 'liczby są podzielne'

print('podaj dwie liczby')

a = int(input())
b = int(input())

if a%b == 0:
    print('liczby są podzielne')
else:
    print('liczby są niepodzielne')
