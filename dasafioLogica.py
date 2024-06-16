# Fazer uma lista para armazenar os produtos inseridos
    produtos = []

    while True:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: R$ "))

        # Adiciona o produto na lista de produtos
        produtos.append((nome, preco))

        continuar = input("Deseja inserir mais produtos? (sim/nao): ")
        if continuar.lower() != 'sim':
            break

    # Inicializa as variáveis para o resumo da compra
    total_gasto = 0.0
    produtos_mais_de_1000 = 0
    produto_mais_barato = None
    preco_mais_barato = float('inf')  # Inicializa com um valor bem alto

    # Processa os produtos para obter o resumo
    for produto in produtos:
        total_gasto += produto[1]  # soma o preço do produto ao total gasto

        if produto[1] > 1000:
            produtos_mais_de_1000 += 1

        if produto[1] < preco_mais_barato:
            preco_mais_barato = produto[1]
            produto_mais_barato = produto[0]

    # Imprime o resumo da compra
    print("\nResumo da Compra:")
    print(f"Total gasto na compra: R$ {total_gasto:.2f}")
    print(f"Quantidade de produtos que custam mais de R$ 1000: {produtos_mais_de_1000}")
    print(f"Nome do produto mais barato: {produto_mais_barato}")

if __name__ == "__main__":
    main()
