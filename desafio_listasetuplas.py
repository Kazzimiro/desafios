# Passo 1: Definir os resultados das equipes
resultados = [
    ("Equipe A", [10, 8, 9]),
    ("Equipe B", [7, 6, 8]),
    ("Equipe C", [9, 9, 9]),
    ("Equipe D", [8, 7, 6]),
]

# Passo 2: Calcular a média das pontuações de cada equipe
medias = []
for equipe, pontuacoes in resultados:
    media = sum(pontuacoes) / len(pontuacoes)
    medias.append(media)

# Passo 3: Ordenar as médias em ordem decrescente
medias.sort(reverse=True)

# Passo 4: Criar a lista de classificação com o nome da equipe e sua média
classificacao = []
for media in medias:
    for equipe, pontuacoes in resultados:
        if sum(pontuacoes) / len(pontuacoes) == media:
            classificacao.append((equipe, media))
            break  # Para evitar adicionar a mesma equipe mais de uma vez

# Exibir a classificação final das equipes
print("Classificação Final:")
for i, (equipe, media) in enumerate(classificacao, start=1):
    print(f"{i}. {equipe}: Média de pontuações = {media:.2f}")
