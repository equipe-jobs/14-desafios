vetor_nomes = []

for i in range(10):
    nome = input(f"Digite o {i+1}º nome: ")
    vetor_nomes.append(nome)

nome_busca = input("Digite um nome para buscar: ")

if nome_busca in vetor_nomes:
    print("ACHEI")
else:
    print("NÃO ACHEI")
