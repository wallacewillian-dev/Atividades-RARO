from enum import Enum, auto
from datetime import datetime

class TipoConta(Enum):
    CONTA_CORRENTE = auto()
    CONTA_POUPANCA = auto()

class Conta:
    def __init__(self, titular, saldo, numero, tipo_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero = numero
        self.tipo_conta = tipo_conta

    def verificar_saldo(self, valor):
        return self.saldo >= valor

    def realizar_pix(self, valor):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

class ContaCorrente(Conta):
    def __init__(self, titular, saldo, numero):
        super().__init__(titular, saldo, numero, TipoConta.CONTA_CORRENTE)
        self.taxa_pix = 0.01

    def realizar_pix(self, valor, mensagem=None):
        valor_total = valor + (valor * self.taxa_pix)
        if self.verificar_saldo(valor_total):
            self.saldo -= valor_total
            print(f"Pix de R${valor} realizado com sucesso! Taxa de R${valor * self.taxa_pix} aplicada.")
        elif mensagem:
                print(f"Mensagem de confirmação: {mensagem}")
        else:
            print("Saldo insuficiente para realizar o Pix.")


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, numero):
        super().__init__(titular, saldo, numero, TipoConta.CONTA_POUPANCA)

    def realizar_pix(self, valor):
        if self.verificar_saldo(valor):
            self.saldo -= valor
            print(f"Pix de R${valor} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o Pix.")

class Pix:
    def __init__(self, conta_origem, conta_destino, valor):
        self.conta_origem = conta_origem
        self.conta_destino = conta_destino
        self.valor = valor
        self.data_hora = datetime.now()

    def realizar(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

class PixSimples(Pix):
    def realizar(self):
        print(f"Realizando Pix Simples de R${self.valor}")
        self.conta_origem.realizar_pix(self.valor)
        self.conta_destino.saldo += self.valor

class PixAgendado(Pix):
    def __init__(self, conta_origem, conta_destino, valor, data_agendada):
        super().__init__(conta_origem, conta_destino, valor)
        self.data_agendada = data_agendada

    def realizar(self):
        if datetime.now() >= self.data_agendada:
            print(f"Realizando Pix Agendado de R${self.valor} na data {self.data_agendada}")
            self.conta_origem.realizar_pix(self.valor)
            self.conta_destino.saldo += self.valor
        else:
            print(f"O Pix agendado está programado para {self.data_agendada}. Aguarde.")


conta1 = ContaCorrente("Wallace Willian", 1000, "12345-6")
conta2 = ContaPoupanca("Elson José", 500, "65432-1")

pix_simples = PixSimples(conta1, conta2, 200)
pix_simples.realizar()

data_agendada = datetime(2024, 12, 25, 12, 0, 0)
pix_agendado = PixAgendado(conta2, conta1, 100, data_agendada)
pix_agendado.realizar()

