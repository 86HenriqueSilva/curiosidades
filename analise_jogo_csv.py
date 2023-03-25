import csv
# criação do dicionário para armazenar os resultados
resultados = {}

# lista de horários com 5 resultados por horário
horarios = ["9 HORAS", "11 HORAS", "12 HORAS", "14 HORAS", "15 HORAS", "17 HORAS", "18 HORAS", "20 HORAS", "21 HORAS"]

# loop para entrada dos resultados de segunda a sábado
for dia in ["SEGUNDA", "TERCA", "QUARTA", "QUINTA", "SEXTA", "SABADO"]:
    resultados[dia] = {}
    for horario in horarios:
        while True:
            try:
                entrada = input(f"Insira os resultados de {dia} no horário das {horario} separados por vírgula (exemplo: 1,2,3,4,5): ")
                numeros = [int(num) for num in entrada.split(",")]
                if len(numeros) != 5:
                    raise ValueError("Número de resultados incorreto. Insira 5 números separados por vírgula.")
                resultados[dia][horario] = numeros
                break
            except ValueError as e:
                print(f"Erro: {e}")

# entrada dos resultados de domingo
resultados["DOMINGO"] = {}
for horario in ["11 HORAS", "12 HORAS", "14 HORAS"]:
    while True:
        try:
            entrada = input(f"Insira os resultados de domingo no horário das {horario} separados por vírgula (exemplo: 1,2,3,4,5): ")
            numeros = [int(num) for num in entrada.split(",")]
            if len(numeros) != 5:
                raise ValueError("Número de resultados incorreto. Insira 5 números separados por vírgula.")
            resultados["DOMINGO"][horario] = numeros
            break
        except ValueError as e:
            print(f"Erro: {e}")

# cálculo da frequência de cada número
frequencia = {}
for dia in resultados:
    for horario in resultados[dia]:
        for numero in resultados[dia][horario]:
            for digito in str(numero):
                if digito not in frequencia:
                    frequencia[digito] = 0
                frequencia[digito] += 1

# adição dos números que não saíram com frequência 0
for numero in range(1, 61):
    if str(numero) not in frequencia:
        frequencia[str(numero)] = 0

# impressão dos números mais, menos e que não saíram
print("Números mais sorteados:")
for numero, freq in sorted(frequencia.items(), key=lambda item: item[1], reverse=True)[:10]:
    print(f"Dígito {numero} foi sorteado {freq} vezes.")

print("\nNúmeros menos sorteados:")
for numero, freq in sorted(frequencia.items(), key=lambda item: item[1])[:10]:
