import RPG as g
def main():
    personagens, erros = g.baixar_personagem('Entrada/entrada.txt')
    
    if erros:
        g.logar_erro('erro.log', [["Erro"]] + erros)

    print("\nPersonagens carregados:")
    for p in personagens:
        print(p)

    while True:
        print("\nEscolha uma opção:")
        print("1. Duelo")
        print("2. Cada um por si")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            print("Duelo iniciado... (em construção)")
        elif opcao == '2':
            print("Modo cada um por si iniciado... (em construção)")
        elif opcao == '3':
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
