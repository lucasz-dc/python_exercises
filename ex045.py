from random import randint

itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(1, 3)

print('\033[1;33m-=-\033[m' * 15)
print('\033[1;40;36m        PEDRA      PAPEL      TESOURA        \033[m')
print('\033[1;33m-=-\033[m' * 15)

print('''Digite \033[1;36;40m[ 1 ]\033[m para jogar PEDRA
Digite \033[1;36;40m[ 2 ]\033[m para jogar PAPEL
Digite \033[1;36;40m[ 3 ]\033[m para jogar TESOURA''')
print('\033[1;33m-=-\033[m' * 15)

jgd = int(input('Qual a sua jogada? '))

if jgd == 1:
    if jgd == 1 == pc:
        print('O jogo deu empate. Ambos escolheram PEDRA!')
    elif jgd == 1 and pc == 2:
        print('O computador venceu. PAPEL vence PEDRA!')
    else:
        print('O jogador venceu. PEDRA vence TESOURA!')

elif jgd == 2:
    if jgd == 2 == pc:
        print('O jogo deu empate. Ambos escolheram PAPEL!')
    elif jgd == 2 and pc == 1:
        print('O jogador venceu. PAPEL vence PEDRA!')
    else:
        print('O computador venceu. TESOURA vence PAPEL!')

elif jgd == 3:
    if jgd == 3 == pc:
        print('O jogo deu empate. Ambos escolheram TESOURA!')
    elif jgd == 3 and pc == 1:
        print('O computador venceu. PEDRA vence TESOURA!')
    else:
        print('O jogador venceu. TESOURA vence PAPEL!')

else:
    print('Comando inálido!')
print('\033[1;33m-=-\033[m' * 15)
