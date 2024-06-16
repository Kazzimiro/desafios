def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return None

def mostrar_menu():
    print("\nEscolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")


    while True:
        mostrar_menu()
        opcao = input("Digite sua escolha (1/2/3/4/5): ")

        if opcao == '5':
            print("Saindo da calculadora. Até mais!")
            break

        if opcao in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                print(f"Resultado: {num1} + {num2} = {soma(num1, num2)}")
            elif opcao == '2':
                print(f"Resultado: {num1} - {num2} = {subtracao(num1, num2)}")
            elif opcao == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicacao(num1, num2)}")
            elif opcao == '4':
                resultado = divisao(num1, num2)
                if resultado is None:
                    print("Erro: Divisão por zero")
                else:
                    print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Opção inválida. Por favor, tente novamente.")
