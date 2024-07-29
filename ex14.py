contagem_tinto = 0
contagem_branco = 0
contagem_rose = 0

total_vinhos = 0

while True:
    tipo_vinho = input("Digite o tipo de vinho (T para tinto, B para branco, R para rosê, ou 0 para encerrar): ").upper()
    
    if tipo_vinho == "0":
        break
    
    if tipo_vinho == "T":
        contagem_tinto += 1
    elif tipo_vinho == "B":
        contagem_branco += 1
    elif tipo_vinho == "R":
        contagem_rose += 1
    else:
        print("Tipo de vinho inválido. Por favor, digite apenas T, B ou R.")
        continue
    
    total_vinhos += 1

if total_vinhos > 0:
    percentual_tinto = (contagem_tinto / total_vinhos) * 100
    percentual_branco = (contagem_branco / total_vinhos) * 100
    percentual_rose = (contagem_rose / total_vinhos) * 100

    print(f"\nTotal de vinhos tinto: {contagem_tinto}")
    print(f"Total de vinhos branco: {contagem_branco}")
    print(f"Total de vinhos rosê: {contagem_rose}")
    print(f"Porcentagem de vinhos tinto: {percentual_tinto:.2f}%")
    print(f"Porcentagem de vinhos branco: {percentual_branco:.2f}%")
    print(f"Porcentagem de vinhos rosê: {percentual_rose:.2f}%")
else:
    print("Nenhum vinho foi registrado.")
