#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    n = int(input('digite um valor: '))

    if n not in lista:
        lista.append(n)
        print(f'({n}) adicionado com sucesso...')
    else:
        print(f'({n}) numero já existe na lista... não sera adcionado')

    op = str(input('Deseja continuar [N/S]? ')).strip().upper()
    if 'N' in op:
        print('lista encerrado...')
        break

for c in range(0, len(lista)):
    print(f'{lista[c]} é o {c + 1}ª item da lista.')
