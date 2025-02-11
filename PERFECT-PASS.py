jogador = int(input('o jogador está com a bola?: 1(s) 2(n):'))
if jogador == 1:
    time = int(input('existe um jogador do seu time livre?: 1(s) 2(n):'))
    if time == 1:
        print('PERFECT PASS')
    else:
        print('fale para um ir, imundo')
else:
    print("tenta pegar a bola >:( ")