#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[] , []]

for c in range(0 , 7):
    num = int(input(f'digite o {c + 1}ª numero: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print('a lista de pares em ordem crescente: ')
lista[0].sort()
for c in range(0 , len(lista[0])):
    print(lista[0][c] , end=' ')

print('\nA lista de impares em ordem crescente: ')
lista[1].sort()
for c in range(0 , len(lista[1])):
    print(lista[1][c] , end=' ')