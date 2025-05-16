from Classe import Guerreiro, Mago, Ladinho
from Personagem import Personagem
from Habilidade import BolaDeFogo, Cura, TiroDeArco
from Arena import Arena
from Log import registrar_log

def mostrar_menu():
    print("\n=== MENU DA ARENA ===")
    print("1 - Adicionar personagem")
    print("2 - Mostrar status dos personagens")
    print("3 - Atacar")
    print("4 - Usar habilidade")
    print("5 - Sair")

def criar_personagem():
    print("Escolha a classe:")
    print("1 - Guerreiro")
    print("2 - Mago")
    print("3 - Ladinho")
    opc = input("Opção: ")
    nome = input("Nome do personagem: ")
    inventario = input("Itens do inventário (separados por vírgula): ").split(',')

    if opc == '1':
        classe = Guerreiro()
    elif opc == '2':
        classe = Mago()
    elif opc == '3':
        classe = Ladinho()
    else:
        print("Opção inválida.")
        return None

    return Personagem(nome.strip(), classe, [item.strip() for item in inventario])

def escolher_personagem(arena, prompt="Escolha um personagem pelo número: "):
    if not arena.personagens:
        print("Nenhum personagem na arena.")
        return None
    for i, p in enumerate(arena.personagens):
        print(f"{i+1} - {p.nome} ({p.classe.nome})")
    try:
        escolha = int(input(prompt)) - 1
        if 0 <= escolha < len(arena.personagens):
            return arena.personagens[escolha]
        else:
            print("Número inválido.")
            return None
    except ValueError:
        print("Entrada inválida.")
        return None

def main():
    arena = Arena()

    habilidades = {
        "bola_de_fogo": BolaDeFogo("Explosão que causa dano em área"),
        "cura": Cura("Restaura pontos de vida"),
        "tiro_de_arco": TiroDeArco("Ataque à distância com arco")
    }

    while True:
        try:
            mostrar_menu()
            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                p = criar_personagem()
                if p:
                    quer_habilidade = input("Quer adicionar uma habilidade? (s/n): ").lower()
                    if quer_habilidade == 's':
                        print("Habilidades disponíveis:")
                        for key in habilidades:
                            print(f"- {key}")
                        hab_nome = input("Digite o nome da habilidade: ").strip().lower()
                        if hab_nome in habilidades:
                            p._Personagem__habilidade = habilidades[hab_nome]
                            print(f"Habilidade {hab_nome} adicionada a {p.nome}")
                        else:
                            print("Habilidade inválida, nenhum efeito adicionado.")
                    arena.adicionar_personagem(p)
                    print(f"{p.nome} adicionado à arena.")

            elif opcao == '2':
                print("\n=== STATUS DOS PERSONAGENS ===")
                print(arena)

            elif opcao == '3':
                atacante = escolher_personagem(arena, "Escolha o atacante: ")
                if atacante:
                    alvo = escolher_personagem(arena, "Escolha o alvo: ")
                    if alvo:
                        print(atacante.atacar(alvo))

            elif opcao == '4':
                usuario = escolher_personagem(arena, "Escolha quem vai usar a habilidade: ")
                if usuario:
                    print(usuario.usar_habilidade())

            elif opcao == '5':
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except Exception as e:
            registrar_log(f"Erro no menu principal: {e}")
            print("Ocorreu um erro. Consulte o arquivo de logs.")

if __name__ == "__main__":
    main()
