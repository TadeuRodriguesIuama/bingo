import random

class Bola:
    def __init__(self, numero):
        self.numero = numero
        self.sorteada = False
    
    def sortear(self):
        self.sorteada = True

class Cartela:
    def __init__(self):
        self.numeros = self.gerarCartela()
    
    def gerarCartela(self):
        numeros = random.sample(range(1, 76), 24)
        return numeros
    
    def marcarNumero(self, numero):
        if numero in self.numeros:
            self.numeros[self.numeros.index(numero)] = 0
    
    def verificarCartela(self):
        return all(numero == 0 for numero in self.numeros)

class Jogo:
    def __init__(self):
        self.cartela = Cartela()
        self.bolasSorteadas = []
    
    def sortearBola(self):
        numero = random.randint(1, 75)
        bola = Bola(numero)
        bola.sortear()
        self.bolasSorteadas.append(bola)
        return bola
    
    def jogar(self):
        while True:
            bola = self.sortearBola()
            print(f'Bola sorteada: {bola.numero}')
            self.cartela.marcarNumero(bola.numero)
            print('Cartela:', self.cartela.numeros)
            if self.cartela.verificarCartela():
                print('Bingo!')
                break

jogo = Jogo()
jogo.jogar()
