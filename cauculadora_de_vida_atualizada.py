import datetime
import calendar

while True:
    try:
        dia, mes, ano, hora = (int(input(f"Informe o {'dia' if i == 0 else 'mês' if i == 1 else 'ano' if i == 2 else 'hora (24 horas)'} de seu nascimento: ")) for i in range(4))

        if not (1 <= mes <= 12) or not (1 <= dia <= calendar.monthrange(ano, mes)[1]) or not (0 <= hora < 24):
            raise ValueError("Data/hora inválida")
        break
    except ValueError as error:
        print("ERRO:", error)

data_nascimento = datetime.datetime(ano, mes, dia, hora, 0, 0)
agora = datetime.datetime.now()
idade = agora - data_nascimento
dias = idade.days
meses = int(dias / 30)
anos = int(dias / 365)
horas = int(idade.total_seconds() / 3600)
periodo = "manhã" if 6 <= hora < 12 else "tarde" if 12 <= hora < 18 else "noite" if 18 <= hora < 24 else "madrugada"
print(f"Você nasceu em {dia} de {calendar.month_name[mes]} de {ano} às {hora} horas da {periodo}.")
print(f"Você tem {dias} dias, {meses} meses e {anos} anos de idade.")
print(f"Você já viveu por aproximadamente {horas} horas.")

vida_restante = 80 - anos
print(f"Estimativamente se tudo ocorrer bem, você ainda tem cerca de {vida_restante} anos de vida." if vida_restante > 0 else "Você já ultrapassou a expectativa média")


