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

def main():
    alunos = []
    
    while True:
        print("\n CADASTRO DE ALUNOS ")
        opcao = input("Digite 1 para cadastrar um aluno ou 0 para sair: ")
        
        if opcao == '0':
            break
        elif opcao == '1':
            aluno = cadastrar_aluno()
            alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")
        else:
            print("Opção indisponível. Por favor, digite novamente.")
    
    print("\n LLISTA DE ALUNOS CADASTRADOS")
    for aluno in alunos:
        print(f"\nNome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Notas: Matemática: {aluno['notas'][0]}, Ciências: {aluno['notas'][1]}, História: {aluno['notas'][2]}")

if __name__ == "__main__":
    main()
