valor_compras_vista = 0
valor_compras_prazo = 0
valor_total_compras = 0

while True:
    codigo = input("Digite o código da transação (V para à vista, P para à prazo): ").upper()
    
    if codigo == "V":
        valor = float(input("Digite o valor da transação: "))
        valor_compras_vista += valor
        valor_total_compras += valor
    elif codigo == "P":
        valor = float(input("Digite o valor da transação: "))
        valor_compras_prazo += valor
        valor_total_compras += valor
    else:
        break 

print(f"\nValor das compras à vista: R$ {valor_compras_vista:.2f}")
print(f"Valor das compras a prazo: R$ {valor_compras_prazo:.2f}")
print(f"Valor total das compras efetuadas: R$ {valor_total_compras:.2f}")
