class Calculadora:
    __area_parede: float
    __area_teto: float

    def calcular_area_parede(self, comodo):
        self.__area_parede = 2 * (comodo.largura + comodo.profundidade) * comodo.altura
        return f"{self.__area_parede}m²"

    def calcular_area_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade
        return f"{self.__area_teto}m²"

    def calcular_litragem(self):
        if self.__area_parede <= 0 or self.__area_teto <= 0:
            return "Impossivel calcular litragem com valores informados"
        else:
            return f"{(self.__area_parede + self.__area_teto) / 10}l"

