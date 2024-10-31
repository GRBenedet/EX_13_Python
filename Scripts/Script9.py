#Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0 , 0 , 0] , [0 , 0 , 0] , [0 , 0 , 0]]
maior = somac = somapares = 0


for l in range(0 , 3):
    for c in range(0  , 3):
        matriz[l][c] = int(input(f'digite um numero pra [{l},{c}]: '))

        if matriz[l][c] % 2 == 0:
            somapares += matriz[l][c]
        if matriz[l][2]:
            somac += matriz[l][2]
        if matriz[1][c] > maior:
            maior = matriz[1][c]

print('='*30)
for l in range(0 , 3):
    for c in range(0 , 3):
        print(f'[{matriz[l][c]:^5}]' , end='')
    print()
print('='*30)

print (f'Esta é a soma de todos os pares: {somapares}.\nEsta é a soma de todos os os numeros da terceira coluna: {somac}.')