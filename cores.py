#verde = 10 reais
#azul = 20 reais
#amarelo = 30 reais
#vermelho = 40 reais
#atribuir preço a cor
#mostrar peço
cor1 = 'verde'
cor2 = 'azul'
cor3 = 'amarelo'
cor4 = 'vermelho'

cor = input ('Qual a cor? ').lower()

if cor == cor1:
    print('R$10')
elif cor == cor2:
    print('R$20')
elif cor == cor3:
    print('R$30')
elif cor == cor4:
    print('R$40')
else:
    print('Cor inválida')

