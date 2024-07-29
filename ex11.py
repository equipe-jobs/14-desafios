N = int(input("Digite um número: "))

if N == 0:
    fatorial = 1
else:
    fatorial = 1
    for i in range(1, N + 1):
        fatorial *= i

print(f"{N}! = {fatorial}")