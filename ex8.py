soma_pares = 0
soma_impares = 0

cont = 0

while cont < 100:
    try:
        numero = int(input(f"Digite o {cont + 1}º número: "))

        if numero % 2 == 0:
            soma_pares += numero
        else:
            soma_impares += numero
        
        cont += 1  
    
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

print(f"\nSoma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")