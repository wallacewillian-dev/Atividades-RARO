class Avaliacao:
    def __init__(self, nota, peso):
        self.nota = nota
        self.peso = peso

    def __repr__(self):
        return f'Avaliacao(nota={self.nota}, peso={self.peso})'

def gerar_melhores_notas(notas):
    notas_relevantes = notas[:3]
    menor_nota = min(notas_relevantes)
    
    if menor_nota < notas[3]:
        index_menor_nota = notas_relevantes.index(menor_nota)
        notas_relevantes[index_menor_nota] = notas[3]
    
    return notas_relevantes

def obter_lista_avaliacoes(notas_relevantes):
    pesos_avaliacoes = [0.4, 0.3, 0.3]
    return [Avaliacao(nota, peso) for nota, peso in zip(notas_relevantes, pesos_avaliacoes)]

def calcular_media(avaliacoes):
    return sum(avaliacao.nota * avaliacao.peso for avaliacao  in avaliacoes)

def obter_status(media):
    status = "aprovado" if media >= 60 else "reprovado"
    return f'Média: {media}\nAluno está {status}!'

notas_aluno = [float(input(f'Digite a nota da {i + 1}° do aluno:\n')) for i in range(4)]

notas_aluno = gerar_melhores_notas(notas_aluno)
avaliacoes = obter_lista_avaliacoes(notas_aluno)
media_aluno = calcular_media(avaliacoes)
status_aluno = obter_status(media_aluno)
print(status_aluno)