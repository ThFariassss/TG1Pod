import RPG as g
import random

def main():
    personagens, erros = g.baixar_personagem('Entrada/entrada.txt')
    
    if erros:
        g.logar_erro('erro.log', [["Erro"]] + erros)

    print("\nPersonagens carregados:")
    for p in personagens:
        print(p)
    arena = g.Arena()

    while True:
        print("\nEscolha uma opção:")
        print("1. Duelo")
        print("2. Cada um por si")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == '1':
            if len(personagens) < 2:
                print("Não há personagens suficientes para um duelo!")
                continue
                
            print("\nEscolha o primeiro personagem:")
            for i, p in enumerate(personagens):
                print(f"{i+1}. {p.nome} ({p.classe.nome})")
                
            try:
                escolha1 = int(input("Personagem 1: ")) - 1
                if escolha1 < 0 or escolha1 >= len(personagens):
                    print("Opção inválida!")
                    continue
                    
                print("\nEscolha o segundo personagem:")
                for i, p in enumerate(personagens):
                    if i != escolha1:
                        print(f"{i+1}. {p.nome} ({p.classe.nome})")
                        
                escolha2 = int(input("Personagem 2: ")) - 1
                if escolha2 < 0 or escolha2 >= len(personagens) or escolha1 == escolha2:
                    print("Opção inválida!")
                    continue   
                arena = g.Arena()
                arena.adicionar_personagem(personagens[escolha1])
                arena.adicionar_personagem(personagens[escolha2])
                print(f"\n## Duelo: {personagens[escolha1].nome} vs {personagens[escolha2].nome}\n")
                vencedor = arena.combate()
                
                print(f"\nO vencedor do duelo foi: {vencedor.nome}!")
                
            except ValueError:
                print("Por favor, digite um número válido!")
                
        elif opcao == '2':
            if len(personagens) < 2:
                print("Não há personagens suficientes para um combate todos contra todos!")
                continue
                
            print("\nEscolha os personagens para o combate (digite 0 para iniciar):")
            
            arena = g.Arena()
            personagens_selecionados = []
            
            while True:
                for i, p in enumerate(personagens):
                    if p not in personagens_selecionados:
                        print(f"{i+1}. {p.nome} ({p.classe.nome})")
                print("0. Iniciar combate")
                
                try:
                    escolha = int(input("Adicionar personagem: "))
                    if escolha == 0:
                        if len(personagens_selecionados) < 2:
                            print("Selecione pelo menos 2 personagens!")
                        else:
                            break
                    elif escolha < 1 or escolha > len(personagens):
                        print("Opção inválida!")
                    else:
                        p = personagens[escolha-1]
                        if p not in personagens_selecionados:
                            personagens_selecionados.append(p)
                            arena.adicionar_personagem(p)
                            print(f"{p.nome} adicionado ao combate!")
                        else:
                            print("Este personagem já foi selecionado!")
                except ValueError:
                    print("Por favor, digite um número válido!")
            
            print("\n## Combate Todos Contra Todos\n")
            vencedor = arena.combate()
            
            print(f"\nO vencedor do combate todos contra todos foi: {vencedor.nome}!")
            
        elif opcao == '3':
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
