#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista =[]

for c in range(0 , 5):
    n = int(input('digite um valor: '))

    if c == 0 or c > lista[-1]:
        lista.append(n)
    else:
        post = 0
        while post < len(lista):
            if n <= lista[post]:
                lista.insert(post, n)
                break
            post += 1

print(lista)