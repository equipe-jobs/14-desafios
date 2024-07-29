soma_pares = 0
quantidade_pares = 0

while True:
    numero = int(input("Digite um número inteiro (ou '0' para encerrar): "))
        
    if numero == 0:
            break
        
    if numero % 2 == 0:
            soma_pares += numero
            quantidade_pares += 1

if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
    print(f"A média dos números pares é: {media_pares:.2f}")
else:
    print("Nenhum número par foi informado.")
