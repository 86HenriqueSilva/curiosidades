frete = {1: "Paulista - R$ 100", 2: "Olinda - R$ 150", 3: "Jaboatao - R$ 200", 4: "Cabo de Santo Agostinho - R$ 250"}

while True:
    escolha = int(input("Informe a opção desejada:\n1 - Paulista\n2 - Olinda\n3 - Jaboatao\n4 - Cabo de Santo Agostinho\nDigite 0 para sair: "))

    if escolha in frete:
        valor_frete = frete[escolha]
        print(f"\n{valor_frete}")
        break
    elif escolha == 0:
        print("\nSaindo do programa...")
        break
    else:
        print("\nPor favor, informe uma opção válida (1 a 4) ou digite 0 para sair.\n")
