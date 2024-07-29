vetor = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

vetor_transformado = []

for i in range(10):
    if i % 2 == 0:  
        novo_valor = vetor[i] // 2
    else:         
        novo_valor = vetor[i] * 3
    vetor_transformado.append(novo_valor)

print("Vetor:")
print(vetor)
print("\nVetor transformado:")
print(vetor_transformado)
