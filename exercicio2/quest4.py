class ContaBancaria:

    def __init__(self, saldo, titular):
        self.titulo = titular
        self.saldo = 0

    def depositar(self, deposito):
        self.saldo = self.saldo + deposito

        print(f'Novo saldo é {self.saldo}')

    def sacar(self, sacar):
        self.saldo = self.saldo - sacar
        print(f'Novo saldo é {self.saldo}')

    conta = ContaBancaria('Amanda', 10)
    conta.depositar(10)
    conta.sacar(10)