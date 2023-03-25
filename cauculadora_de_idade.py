import datetime

# Solicita a data de nascimento ao usuário
while True:
    try:
        day = int(input("Informe o dia de nascimento: "))
        month = int(input("Informe o mês de nascimento: "))
        year = int(input("Informe o ano de nascimento: "))
        hour = int(input("Informe a hora de nascimento (2 dígitos): "))
        break
    except ValueError:
        print("Por favor, informe apenas números.")

# Cria um objeto de data de nascimento
birth_date = datetime.datetime(year, month, day, hour, 0, 0)

# Calcula a idade atual
now = datetime.datetime.now()
age = now - birth_date

# Calcula a idade em dias, meses e anos
days = age.days
months = int(days / 30.44)
years = int(days / 365.25)
hours = int(age.total_seconds() / 3600)

# Imprime o resultado
print("Você já viveu", days, "dias,", months, "meses,", years, "anos e", hours, "horas.")
