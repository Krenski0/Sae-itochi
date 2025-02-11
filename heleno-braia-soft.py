

jogador = int(input('o jogador está com a bola?: 1(s) 2(n):'))
if jogador == 1:
    print("perfeito")
else:
    print("tenta pegar a bola >:( ")

heleno_braia = int(input('heleno está no jogo? 1(s) 2(n):'))
if heleno_braia == 1:
    livre = int(input('heleno está livre? 1(s) 2(n)'))
    if livre == 1:
        print("PERFECT PASS NO HELENOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    else:
        print('PERFECT PASS NO HELENO FDS')
else:
    print('siga o protocolo sem o heleno')
