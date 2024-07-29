numeros = []
while True:
    entrada = input("Digite um número (ou 'fim' para encerrar a entrada): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

pares.sort()

impares.sort(reverse=True)

resultado = pares + impares
print("\nNúmeros organizados:", resultado)
