import random 
lista = ['Fulano', 'Ciclano', 'Beltrano']

sorteado = random.sample(lista, 1)

for i in sorteado:
    print(f'O sorteado foi {i}')
