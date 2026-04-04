class Cachorro:
    def __init__(self,nome,cor,acordado=True):
        print("Inicializando a classe ...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instancia da classe")


    def falar(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("zeus","preto", False)
    print(c.nome)

c = Cachorro("Chappie","amarelo")
c.falar()


print("po")
print("po")
del c
print("po")
print("po")
print("po")
print("po")
print("po")

#criar_cachorro()