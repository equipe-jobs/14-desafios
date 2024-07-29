vetor = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

print("Vetor:")
print(vetor)

print("\nVetor reverso:")
print(vetor[::-1]) 
