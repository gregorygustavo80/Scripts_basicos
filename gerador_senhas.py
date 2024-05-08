import random

numeros = [0, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letras_maiusculas = [letra.upper() for letra in letras]
caracter_especial = ['@','#','$','%','&','*']

def x(numeros):
    return random.sample(numeros, 2)

def y(letras):
    return random.sample(letras, 3)

def z(letras_maiusculas):
    return random.sample(letras_maiusculas, 2)

def i(caracter_especial):
    return random.sample(caracter_especial, 2)

listas = (
    ''.join(str(num) for num in x(numeros)) + 
    ''.join(y(letras)) + 
    ''.join(z(letras_maiusculas)) + 
    ''.join(i(caracter_especial))
)

senha = ''.join(random.sample(listas, len(listas)))

print(senha)