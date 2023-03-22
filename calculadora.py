class Calculadora:
    largura: float
    profundidade: float
    altura: float = 2.9
    area_parede: float
    area_teto: float

    def __init__(self, largura: float, profundidade: float, altura: float = 2.9):
        self.largura = largura
        self.profundidade = profundidade
        self.altura = altura

    def calcular_area_parede(self):
        self.area_parede = 2 * (self.largura + self.profundidade) * self.altura
        return self.area_parede

    def calcular_area_teto(self):
        return self.largura * self.profundidade

    def calcular_litragem(self):
        return (self.calcular_area_parede() + self.calcular_area_teto()) / 2





