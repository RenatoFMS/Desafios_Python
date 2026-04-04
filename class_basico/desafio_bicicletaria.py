class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
       self.cor = cor
       self.modelo = modelo
       self.ano = ano
       self.valor = valor

    def buzinar(self):
        print("Plin plin ...")

    def parar (self):
        print("Parando bicicleta ...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmmmm...")

    def __str__(self):
       return f"Bicicleta: cor = {self.cor}, modelo ={self.modelo},ano = {self.ano}, valor = {self.valor}"

b1 = Bicicleta("vermelho","coloi",2022,600)

b1.buzinar()
b1.correr()
b1.parar()

print(b1.modelo,b1.cor,b1.ano,b1.valor)


b2 = Bicicleta("verde","monark",2000,198)

b2.buzinar

print(b2)