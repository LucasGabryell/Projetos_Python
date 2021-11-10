from random import randint

numero = int(randint(1, 100))
resultado = 0
while resultado != numero:
    resultado = int(input('Digite um número: '))
    if resultado < 0 or resultado > 100:
        print("O número está entre 0 e 100!")
    if resultado > numero:
        print("Digite um número menor!")
    elif resultado < numero:
        print("Digite um número maior!")
    elif resultado == numero:
        print(f"Voce acertou, resultado: {numero}")