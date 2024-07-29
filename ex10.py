n = int(input("Digite um número: "))

contador = 1

for i in range(1, n + 1):
    for j in range(i):  
        print(contador,  end= ' ')
        contador += 1
    print()