from calculadora import Calculadora
from comodo import Comodo

comodo1 = Comodo(
    input("Qual largura: "),
    input("Qual profundidade: ")
)

calc = Calculadora()
print(f"Área parede: {calc.calcular_area_parede(comodo1)}")
print(f"Área teto: {calc.calcular_area_teto(comodo1)}")
print(f"Litragem de tinta: {calc.calcular_litragem()}")
