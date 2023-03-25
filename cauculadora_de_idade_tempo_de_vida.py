import datetime

# Solicita a data de nascimento ao usuário
# Solicita a data de nascimento ao usuário
while True:
    try:
        dia = int(input("Informe o dia do seu nascimento: "))
        mes = int(input("Informe o mês do seu nascimento (2 dígitos): "))
        ano = int(input("Informe o ano do seu nascimento: "))
        hora = int(input("Informe a hora do seu nascimento (2 dígitos): "))
        if mes < 1 or mes > 12:
            raise ValueError("O mês informado é inválido.")
        break
    except ValueError as error:
        print("ERRO:", error)

# Cria um objeto de data de nascimento
data_nascimento = datetime.datetime(ano, mes, dia, hora, 0, 0)

# Calcula a idade atual
agora = datetime.datetime.now()
idade = agora - data_nascimento

# Calcula a idade em dias, meses e anos
dias = idade.days
meses = int(dias / 30.44)
anos = int(dias / 365.25)
horas = int(idade.total_seconds() / 3600)

# Define se é manhã ou noite
if hora >= 6 and hora < 12:
    período = "manhã"
elif hora >= 12 and hora < 18:
    período = "tarde"
elif hora >= 18 and hora < 24:
    período = "noite"
else:
    período = "madrugada"

# Imprime o resultado
print("Você nasceu em", dia, "de", mes, "de", ano, "às", hora, "horas da", período)
print("Você já viveu", dias, "dias,", meses, "meses,", anos, "anos e", horas, "horas.")

# Estimativa de vida ainda por viver
vida_restante = 80 - anos

if vida_restante > 0:
    print("Acaso não lhe falte sorte, Você ainda tem cerca de", vida_restante, "anos de vida.")
else:
    print("Você já viveu mais do que a média de vida atual.")
