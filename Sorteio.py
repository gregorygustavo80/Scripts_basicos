import random

nomes_participantes = []
entrada_nomes = input("Digite os nomes separados por vírgula: ")

if entrada_nomes.strip() == '':
    pass
else:
    nomes_participantes.extend([nome.strip() for nome in entrada_nomes.split(',')])


if not nomes_participantes:
    print("Nenhum nome foi fornecido.")
else:
    confirmacao_sorteio = input('Digite [S] para sortear: ')
    
    if confirmacao_sorteio.upper() == 'S' or confirmacao_sorteio.upper == 's':
        sorteado = random.choice(nomes_participantes)
        print(f'O sorteado foi {sorteado}')
    else:
        print("O sorteio não foi realizado.")
