class Tabla:
    def __init__(self,numero):
        self.numero = numero

    def mostrarNormal(self):
        for i in range(1,11):
            print(f"{self.numero}X{i}={self.numero * i}")

    def mostarInvertido(self):
        for i in range(10,0,-1):
            print(f"{self.numero}X{i}={self.numero * i}")

