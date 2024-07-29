vetor1 = []
vetor2 = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor1.append(numero)

for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor2.append(numero)

vetor_diferenca = []
vetor_soma = []
vetor_multiplicacao = []

for i in range(20):
    diferenca = vetor1[i] - vetor2[i]
    soma = vetor1[i] + vetor2[i]
    multiplicacao = vetor1[i] * vetor2[i]
    
    vetor_diferenca.append(diferenca)
    vetor_soma.append(soma)
    vetor_multiplicacao.append(multiplicacao)

print("\nVetor da diferença:")
print(vetor_diferenca)
print("\nVetor da soma:")
print(vetor_soma)
print("\nVetor da multiplicação:")
print(vetor_multiplicacao)
