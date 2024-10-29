#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []
op = ''

while True:
    lista.append(int(input('digite um valor: ')))
    
    op = str(input('deseja continuar [N/S]? ')).strip().upper()
    if 'N' in op:
        print('lista finalizada...')
        break
for c in range(0 , len(lista)):

    if c % 2 == 0:
        lista_par.append(lista[c])

    else:
        lista_impar.append(lista[c])

print('Está é sua lista: ' , end='')
for c in range(0 , len(lista)):
    print(lista[c] , end=' ')

print('\nEstes são os pares de sua lista: ' , end='')
for c in range(0 , len(lista_par)):
    print(lista_par[c] , end=' ')

print('\nEste são os impares da sua lista: ' , end='')
for c in range(0 , len(lista_impar)):
    print(lista_impar[c] , end=' ')
