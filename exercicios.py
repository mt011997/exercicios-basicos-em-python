# 1- Faça um programa que leia  um número inteiro e o imprima.
numExe1 = 10
print(f'Número inteiro: {numExe1}')

# 2- Faça um programa que leia um número real e o imprima.
numRealExe2 = 10.50
print(f"Número real: {numRealExe2}")

# 3- Peça ao usuário  para digitar 3 valores inteiros e imprima a soma deles.
num1Exe3 = int(input('Digite um número inteiro '))
num2Exe3 = int(input('Digite outro número inteiro '))
num3Exe3 = int(input('Digite mais um número inteiro '))
resultadoExe3 = num1Exe3 + num2Exe3 + num3Exe3
print(f'A soma total dos números digitados é de: {resultadoExe3}')

# 4- Leia um número real e imprima o quadrado desse número.
numRealExe4 = 8.50
resultadoExe4 = numRealExe4 ** 2
print(f'8.50 elevado a 2 é: {resultadoExe4}')

# 5 - Leia um número real e imprima a quinta parte desse número.
numRealExe5 = 37.83
resultadoExe5 = numRealExe5 / 5
print(f'A quinta parte de 37.83 é de: {resultadoExe5}')

# 6- Leia uma temperatura em Celsius e converta para Fahrenheit.
tempExe6 =  20.0
fahrenheitExe6 = tempExe6 * (9.0 / 5.0) + 32.0
print(f'{tempExe6}°C em fahrenheit, fica: {fahrenheitExe6}°F')

# 7- Leia uma temperatura em Fahrenheit e converta para Celsius.
tempExe7 = 68.0
celsiusExe7 = 5.0 * (tempExe7 - 32.0) / 9.0
print(f'{tempExe7}°F em celsius, fica: {celsiusExe7}°C')

# 8- Leia uma temperatura em Kelvin e converta para Celsius.
tempExe8 = 293.15
celsiusExe8 = tempExe8 - 273.15
print(f'{tempExe8}°K em celsius, fica: {celsiusExe8}°C')

# 9- Leia uma temperatura em Celsius e converta para Kelvin
tempExe9 = 20.0
kelvinExe9 = tempExe9 + 273.15
print(f'{tempExe9}°C em kelvin, fica: {kelvinExe9}°K')

# 10- Leia uma velocidade em Km/h e converta em m/s
kmExe10 = 60
metrosExe10 = kmExe10 / 3.6
print(f'{kmExe10}km/h em metros por segundo é: {metrosExe10}m/s')
