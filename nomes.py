# criar um programa um que obtem o nome e sobrenome a partir da entrada do usuário e retorna a mensagem "Meu nome é (nome completo)"
nome = input('Qual seu nome? ')
sobrenome = input('Qual seu sobrenome? ')
print('Meu nome é', nome, sobrenome)

# 1° forma: concatenando utilizando o operador +
print('Meu nome é ' + nome + ' ' + sobrenome)

# 2° forma: utilizando a virgula para chamar as variáveis
print('Meu nome é', nome, sobrenome)

#3° forma: utilizando o fstring
print(f'Meu nome é {nome} {sobrenome}')