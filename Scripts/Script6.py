#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

f = str(input('digite um expresão: '))

aberto = fechado = 0

for c in f:
    if c == ')':
        aberto += 1
    elif c == '(':
        fechado += 1

if aberto == fechado:
    print('sua expreção é valida!')
else:
    print('sua expreção é invalida')
