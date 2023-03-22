from calculadora import Calculadora

largura_area = float(input("Qual largura: "))
profundidade_area = float(input("Qual profundidade: "))

calc = Calculadora(largura_area, profundidade_area)
print(calc.calcular_area_parede())
