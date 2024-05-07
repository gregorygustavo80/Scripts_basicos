def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida"
    else:
        return x / y

print("Selecione a operação desejada:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Escolha uma opção (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    print(num1, "+", num2, "=", adicao(num1, num2))
elif escolha == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))
elif escolha == '3':
    print(num1, "*", num2, "=", multiplicao(num1, num2))
elif escolha == '4':
    print(num1, "/", num2, "=", divisao(num1, num2))
else:
    print("Entrada inválida")