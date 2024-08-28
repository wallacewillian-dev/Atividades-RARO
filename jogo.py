import random

def jogo (escolha_jogador):
    opcoes = ["rock", "paper", "scissors", "spock", "lizard"]
    escolha_computador = random.choice(opcoes).lower()
    
    print(f"Player chooses {escolha_jogador}")
    print(f"Computer chooses {escolha_computador}")
    
    if escolha_jogador == escolha_computador:
        return "Player and computer tie!"
    elif (escolha_jogador == "rock" and escolha_computador in ["scissors", "lizard"]) or \
         (escolha_jogador == "paper" and escolha_computador in ["rock", "spock"]   ) or \
         (escolha_jogador == "scissors" and escolha_computador in ["paper", "lizard"]) or \
         (escolha_jogador == "spock"   and escolha_computador in ["rock", "scissors"]) or \
         (escolha_jogador == "lizard" and escolha_computador in ["paper", "spock"] ):
        return "Player wins!"
    else:
        return "Computer wins!"
print('''
    -Rock
    -Paper
    -Scissors
    -Spock
    -Lizard
      ''')
escolha = input("What's your choice? ").lower()
resultado = jogo (escolha)
print(resultado)