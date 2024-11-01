#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
numsorte = []
lista = []
jogos = 1
print(f'{'=' * 49}')
quant = int(input('quantos jogos deseja sortear? '))

while jogos <= quant:
    for c in range(0 , 6):
        
        num = randint(1 , 60)
        if num not in numsorte:
            numsorte.append(num)
    lista.append(numsorte[:])
    numsorte.clear()
    jogos +=1

print(f'{'='*15} SORTEANDO {quant} JOGOS {'='*15}')
for i , l in enumerate(lista):
    print(f'{i + 1}ª jogo sorteado: {l}')
print(f'{'=' * 49}')