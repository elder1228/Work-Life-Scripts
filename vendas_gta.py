def calcular_venda():
    print("\n" + "="*30)
    print("🚗 SISTEMA DE VENDAS - PREMIUM")
    print("="*30)
    
    # Entrada de dados
    nome_veiculo = input("Nome do Veículo: ")
    valor_base = float(input("Valor de Tabela (R$): "))
    
    print("\nCategorias: [1] Popular | [2] Esportivo | [3] Super")
    categoria = input("Escolha a categoria: ")

    # Lógica de Impostos (Baseado no seu README)
    if categoria == "1":
        imposto = 0.05  # 5%
        tipo = "Popular"
    elif categoria == "2":
        imposto = 0.10  # 10%
        tipo = "Esportivo"
    else:
        imposto = 0.15  # 15%
        tipo = "Super"

    # Cálculos
    valor_imposto = valor_base * imposto
    preco_final = valor_base + valor_imposto
    comissao = preco_final * 0.02  # 2% de comissão conforme seu README

    # Exibição do Recibo
    print("\n--- 📄 RECIBO DE VENDA ---")
    print(f"Veículo: {nome_veiculo} ({tipo})")
    print(f"Valor Base: R$ {valor_base:,.2f}")
    print(f"Imposto ({int(imposto*100)}%): R$ {valor_imposto:,.2f}")
    print(f"PREÇO FINAL: R$ {preco_final:,.2f}")
    print(f"Sua Comissão (2%): R$ {comissao:,.2f}")
    print("-" * 25)

if __name__ == "__main__":
    while True:
        calcular_venda()
        continuar = input("\nNova venda? (s/n): ")
        if continuar.lower() != 's':
            break
