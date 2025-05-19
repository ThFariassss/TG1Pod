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
        print("3. Criar Personagem")
        print("4. Sair")

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
            print("\n## Criar Novo Personagem ##")
            
            # Solicitar nome do personagem
            nome = input("Digite o nome do personagem: ")
            
            # Solicitar classe do personagem
            print("\nEscolha a classe do personagem:")
            print("1. Guerreiro")
            print("2. Mago")
            print("3. Ladino")
            
            try:
                escolha_classe = int(input("Classe: "))
                if escolha_classe < 1 or escolha_classe > 3:
                    print("Opção de classe inválida!")
                    continue
                
                classes = ["Guerreiro", "Mago", "Ladino"]
                classe_nome = classes[escolha_classe - 1]
                
                # Definir limite de habilidades com base na classe
                limite_habilidades = 2 if classe_nome == "Guerreiro" else (5 if classe_nome == "Mago" else 3)
                
                # Solicitar habilidades
                print(f"\nEscolha até {limite_habilidades} habilidades (digite 0 para finalizar):")
                print("1. BolaDeFogo")
                print("2. Cura")
                print("3. Tiro de Arco")
                print("0. Finalizar seleção")
                
                habilidades_disponiveis = ["BolaDeFogo", "Cura", "Tiro de Arco"]
                habilidades_selecionadas = []
                
                while len(habilidades_selecionadas) < limite_habilidades:
                    try:
                        escolha_hab = int(input(f"Habilidade {len(habilidades_selecionadas) + 1}: "))
                        
                        if escolha_hab == 0:
                            if len(habilidades_selecionadas) == 0:
                                print("Selecione pelo menos uma habilidade!")
                            else:
                                break
                        elif escolha_hab < 1 or escolha_hab > 3:
                            print("Opção de habilidade inválida!")
                        else:
                            habilidade = habilidades_disponiveis[escolha_hab - 1]
                            if habilidade in habilidades_selecionadas:
                                print("Esta habilidade já foi selecionada!")
                            else:
                                habilidades_selecionadas.append(habilidade)
                                print(f"Habilidade {habilidade} adicionada!")
                                
                                # Perguntar se deseja adicionar mais habilidades
                                if len(habilidades_selecionadas) < limite_habilidades:
                                    continuar = input("Deseja adicionar mais habilidades? (s/n): ").lower()
                                    if continuar != 's':
                                        break
                    except ValueError:
                        print("Por favor, digite um número válido!")
                
                # Criar o personagem
                resultado, mensagem = g.criar_personagem('Entrada/entrada.txt', nome, classe_nome, habilidades_selecionadas)
                
                if resultado:
                    print(f"\n{mensagem}")
                    print("Recarregando lista de personagens...")
                    
                    # Recarregar a lista de personagens para incluir o novo
                    personagens, erros = g.baixar_personagem('Entrada/entrada.txt')
                    if erros:
                        g.logar_erro('erro.log', [["Erro"]] + erros)
                    
                    print("\nPersonagens atualizados:")
                    for p in personagens:
                        print(p)
                else:
                    print(f"\nErro ao criar personagem: {mensagem}")
                
            except ValueError:
                print("Por favor, digite um número válido!")
            
        elif opcao == '4':
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
