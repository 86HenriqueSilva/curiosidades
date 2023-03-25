from datetime import datetime


class Sensor:
    def __init__(self, nome):
        self.nome = nome
        self.dados = []

    def registrar(self, valor):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.dados.append((valor, timestamp))


class SensorTemperatura(Sensor):
    def __init__(self):
        super().__init__("Temperatura")


class SensorUmidade(Sensor):
    def __init__(self):
        super().__init__("Umidade")


class SensorCO2(Sensor):
    def __init__(self):
        super().__init__("CO2")


class Ambiente:
    def __init__(self):
        self.sensor_temperatura = SensorTemperatura()
        self.sensor_umidade = SensorUmidade()
        self.sensor_co2 = SensorCO2()

    def registrar_todos_os_sensores(self, valor_temperatura, valor_umidade, valor_co2):
        self.sensor_temperatura.registrar(valor_temperatura)
        self.sensor_umidade.registrar(valor_umidade)
        self.sensor_co2.registrar(valor_co2)

    def obter_ultimas_leituras(self):
        temperatura = self.sensor_temperatura.dados[-1][0]
        umidade = self.sensor_umidade.dados[-1][0]
        co2 = self.sensor_co2.dados[-1][0]
        return (temperatura, umidade, co2)

    def imprimir_dados_ordenados(self):
        dados = [self.sensor_temperatura.dados, self.sensor_co2.dados, self.sensor_umidade.dados]
        nomes = [self.sensor_temperatura.nome, self.sensor_co2.nome, self.sensor_umidade.nome]
        ordens_de_ordenacao = ["asc", "asc", "desc"]

        for i in range(len(dados)):
            print(f"Dados de {nomes[i]} ordenados em ordem {ordens_de_ordenacao[i]}:")
            dados_ordenados = sorted(dados[i], key=lambda x: x[0], reverse=(ordens_de_ordenacao[i] == "desc"))
            for valor, timestamp in dados_ordenados:
                print(f"{valor:.2f} em {timestamp}")
            print("")


if __name__ == "__main__":
    ambiente = Ambiente()
    ambiente.registrar_todos_os_sensores(25.3, 0.48, 800)
    ambiente.registrar_todos_os_sensores(26.0, 0.49, 810)
    ambiente.registrar_todos_os_sensores(26.5, 0.47, 820)
    ambiente.imprimir_dados_ordenados()
