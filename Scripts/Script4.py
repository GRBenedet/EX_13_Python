#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0

while True:
    lista.append(int(input('digite um valor: ')))
    cont +=1

    op = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if 'N' in op:
        print('lista fechada...')
        break

print(f'Sua lista tem {cont} numeros.')

print('essa ord0em padrão de sua lista: ' , end='')
for c in range(0 , len(lista)):
    print(lista[c] , end=' ')


print(f'e essa em forma decresente ' , end='')
lista.sort(reverse=True)
for c in range(0 , len(lista)):
    print(lista[c] , end=' ')

if 5 in lista:
    print(f'\nO numero 5 foi digitado.')
else:
    print('\nO numero 5 não foi digitado.')