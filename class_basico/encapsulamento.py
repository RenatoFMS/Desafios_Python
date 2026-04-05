class Conta:
    def __init__(self, nro_agencia, saldo = 0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self,valor):
        self._saldo += valor

    def sacar(self,valor):
        self._saldo += valor

    def mostar_saldo(self):
        return self._saldo


conta = Conta("212",100)
conta.depositar(100)
print(conta.mostar_saldo)
print(conta.nro_agencia)