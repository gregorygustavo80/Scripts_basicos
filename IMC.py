def imc(peso,altura):
     return peso/(altura**2)

nome = (input('Digite seu nome:')).strip().title()
peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura: '))

imc = peso/(altura**2)

print(f'{nome}, seu índice de massa corporal é: {imc:.2f}')

if imc < 16:
    print(f'{nome}, você tem magreza grave')
elif 16 <= imc < 16.9:
    print(f'{nome}, você tem magreza moderada')
elif 16.9 <= imc < 18.5:
    print(f'{nome}, você tem magreza leve')
elif 18.5 <= imc < 25:
    print(f'{nome}, você está com peso normal')
elif 25 <= imc < 30:
    print(f'{nome}, você está com sobrepeso')
elif 30 <= imc < 35:
    print(f'{nome}, você está com obesidade grau 1')
elif 35 <= imc < 40:
    print(f'{nome}, você está com obesidade grau 2 (severa)')
else:
    print(f'{nome}, você está com obesidade grau 3 (mórbida)')

input("Pressione Enter para sair...")
