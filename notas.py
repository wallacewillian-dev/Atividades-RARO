nota1 =float(input('Digite sua primeira nota: '))
nota2 =float(input('Digite sua segunda nota: '))
nota3 =float(input('Digite sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >=0 and media <5:
    print(f'Você foi reprovado, sua nota é {media:.1f}')
elif media >=5 and media <7:
    print(f'Você está em recuperação, sua nota é {media:.1f}')
else:
    print(f'Você foi aprovado, sua nota é {media:.1f}')