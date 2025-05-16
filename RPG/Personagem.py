from Classe import Classe
from Dado import Dado

class Personagem:
    qtd_instancias = 0

    def __init__(self, nome: str, classe: Classe, inventario: list):
        self.__nome = nome
        self.__classe = classe 
        self.__inventario = inventario
        self.__habilidade = None  
        Personagem.qtd_instancias += 1

    def __str__(self):
        inventario_str = ', '.join(self.__inventario) if self.__inventario else "Vazio"
        return (f'Personagem: {self.__nome} ({self.__classe.nome})\n'  
                f'Pontos de Vida: {self.__classe.pontos_vida}\n' 
                f'Ataque: {self.__classe.pontos_ataque}\n'
                f'Defesa: {self.__classe.pontos_defesa}\n'
                f'Inventário: {inventario_str}')

    def __repr__(self):
        return f'Personagem(nome={self.__nome}, classe={self.__classe}, inventario={self.__inventario})'

    def __eq__(self, other):
        if isinstance(other, Personagem):
            return self.__nome == other.__nome and self.__classe == other.__classe
        return False

    @property
    def nome(self):
        return self.__nome

    @property
    def classe(self):
        return self.__classe

    @classe.setter
    def classe(self, nova_classe):
        self.__classe = nova_classe

    @property
    def inventario(self):
        return self.__inventario

    @inventario.setter
    def inventario(self, novo_inventario):
        self.__inventario = novo_inventario

    def atacar(self, alvo):
        """Método para atacar um alvo."""
        if isinstance(alvo, Personagem):
            dano_base = self.__classe.pontos_ataque + self.__classe.dado_de_ataque.jogar()
            dano_final = max(0, dano_base - alvo.classe.pontos_defesa)
            alvo.classe._Classe__pontos_vida -= dano_final  # acessar atributo privado de forma controlada
            return f'{self.__nome} atacou {alvo.nome} e causou {dano_final} de dano!'
        else:
            return "Alvo inválido!"

    def usar_habilidade(self):
        """Método para usar uma habilidade (caso tenha)."""
        if self.__habilidade:
            return self.__habilidade.usar()
        else:
            return "Nenhuma habilidade disponível!"
