class Veiculo:
    def __init__(self,cor,placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self,cor,placa,numero_rodas,carregado):
        super().__init__(cor,placa,numero_rodas)
        self.carregado = carregado
    def esta_carregado(self):
        print(f"{"Sim" if self.carregado else "Não"} esta carregado")

moto = Motocicleta("preta","abc-1234",2)

print(moto)
moto.ligar_motor()

carro = Carro("branco","dep-0342",4)
carro.ligar_motor()


Caminhao = Caminhao("amarelo","art-3045",10,True)
Caminhao.ligar_motor()
Caminhao.esta_carregado()

print(Caminhao)
