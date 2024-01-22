from area import Retangulo
import math

while True:
    piso_a = float(input("Digite o lado do primeiro piso: "))
    piso_b = float(input("Digite o outro lado: "))

    piso = Retangulo(piso_a, piso_b)

    az_a = float(input("Digite o lado do primeiro azulejo: "))
    az_b = float(input("Digite o outro lado: "))

    azulejo = Retangulo(az_a, az_b)

    area_piso = piso.area()
    area_az = azulejo.area()

    qntd_az = area_piso / area_az

    if area_piso % area_az == 0:
        print(f'A quantidade exata de azulejos que você precisa para preencher é de: {qntd_az} Azulejos')
    else:
        print(f'A quantidade minima para você preencher com azulejos é de: {math.ceil(qntd_az)}')