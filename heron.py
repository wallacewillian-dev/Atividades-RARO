import math

def area_triangulo(ponto1, ponto2, ponto3):
    lado1 = math.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)
    lado2 = math.sqrt((ponto2[0] - ponto3[0])**2 + (ponto2[1] - ponto3[1])**2)
    lado3 = math.sqrt((ponto3[0] - ponto1[0])**2 + (ponto3[1] - ponto1[1])**2)

    semi = (lado1 + lado2 + lado3) / 2

    area = math.sqrt(semi * (semi-lado1) * (semi - lado2) * (semi - lado3))
    
    return f'A triangle with vertices {ponto1}, {ponto2}, and {ponto3} has an area of {area:.1f}.'

ponto1 = (0,0)
ponto2 = (3,4)
ponto3 = (1,1)


print(area_triangulo(ponto1, ponto2, ponto3))
