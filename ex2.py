vetor = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

vetor_inverso = vetor[::-1]

print("Vetor:")
print(vetor)
print("\nVetor invertido:")
print(vetor_inverso)
