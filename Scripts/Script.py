#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = list()
maior = 0
menor = 0
for c in range(0 , 5):
    valores.append(int(input(f'digite o {c + 1}ª valor: ')))
    if c == 0:
        maior = menor = valores[c]
    if valores[c] < menor:
        menor = valores[c]
    elif valores[c] > maior:
        maior = valores[c]

print(f'A sua lista é: ')
for c in range(0 , len(valores)):
    print(f'{valores[c]}' , end=' ')

print(f'\nTendo como maior numero o {maior} que esta nas posições:' , end=' ')
for i , c in enumerate(valores):
    if c == maior:
        print(f'{i + 1}ª...' , end=' ')

print(f'\nTendo como menor numero o {menor} que esta nas posições:' , end=' ')
for i , c in enumerate(valores):
    if c == menor:
        print(f'{i + 1}ª...' , end=' ')