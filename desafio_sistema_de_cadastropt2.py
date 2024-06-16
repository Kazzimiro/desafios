def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    matematica = float(input("Digite a nota de Matemática: "))
    ciencias = float(input("Digite a nota de Ciências: "))
    historia = float(input("Digite a nota de História: "))

    aluno = {
        'nome': nome,
        'idade': idade,
        'notas': (matematica, ciencias, historia)
    }
    
    return aluno

def exibir_alunos(alunos):
    print("\nLISTA DE ALUNOS CADASTRADOS")
    for aluno in alunos:
        print(f"\nNome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Notas: Matemática: {aluno['notas'][0]}, Ciências: {aluno['notas'][1]}, História: {aluno['notas'][2]}")
        print(f"Média das notas: {calcular_media(aluno['notas']):.2f}")

def calcular_media(notas):
    return sum(notas) / len(notas)

def encontrar_melhor_aluno(alunos):
    melhor_media = -1
    melhor_aluno = None
    
    for aluno in alunos:
        media = calcular_media(aluno['notas'])
        if media > melhor_media:
            melhor_media = media
            melhor_aluno = aluno
    
    return melhor_aluno

def main():
    alunos = []
    
    while True:
        print("\nMENU PRINCIPAL")
        print("1. Cadastrar aluno")
        print("2. Visualizar alunos cadastrados")
        print("3. Exibir média das notas de cada aluno")
        print("4. Identificar aluno com melhor média")
        print("0. Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '0':
            print("Encerrando o programa...")
            break
        elif opcao == '1':
            aluno = cadastrar_aluno()
            alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")
        elif opcao == '2':
            exibir_alunos(alunos)
        elif opcao == '3':
            exibir_medias_alunos(alunos)
        elif opcao == '4':
            melhor_aluno = encontrar_melhor_aluno(alunos)
            if melhor_aluno:
                print(f"\nALUNO COM MELHOR MÉDIA: {melhor_aluno['nome']}")
                print(f"Média das notas: {calcular_media(melhor_aluno['notas']):.2f}")
            else:
                print("Nenhum aluno cadastrado.")
        else:
            print("Opção inválida. Por favor, digite novamente.")

def exibir_medias_alunos(alunos):
    print("\nMÉDIA DAS NOTAS DOS ALUNOS")
    for aluno in alunos:
        print(f"{aluno['nome']}: {calcular_media(aluno['notas']):.2f}")

if __name__ == "__main__":
    main()
