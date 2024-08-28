numero1 =input('Primeiro? ')
numero2 =input('Segundo? ')
numero3 =input('Terceiro? ')

if numero1 > numero2 and numero1 > numero3:
    print(f'O numero maior é o {numero1}')
elif numero2 > numero1 and numero2 > numero3:
    print(f'O numero maior é o {numero2}')
elif numero3 > numero2 and numero3 > numero1:
    print(f'O numero maior é o {numero3}')
