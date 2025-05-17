from .Classe import *
from .Erros import *
from .Habilidade import *

class Personagem:
    qtd_instancias = 0

    def __init__(self, nome, classe, inventario ):
        self.__nome = nome
        self.__classe = classe 
        self.__inventario = inventario 
        Personagem.qtd_instancias += 1

    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def classe(self):
        return self.__classe

    @classe.setter
    def classe(self, nova_classe):
        if isinstance(nova_classe, Classe):
            self.__classe = nova_classe
        else:
            raise ClasseInvalida("Classe deve ser uma instância da classe Classe.")

    @property
    def inventario(self):
        return self.__inventario

    @inventario.setter
    def inventario(self, novo_inventario):
        self.__inventario = novo_inventario

    @staticmethod
    def logar_personag(nome, classe_nome, habilidades):
        """
        Método estático para criar um personagem a partir de dados carregados.
        
        Args:
            nome (str): Nome do personagem
            classe_nome (str): Nome da classe do personagem
            habilidades (list): Lista de nomes de habilidades
            
        Returns:
            Personagem: Instância de personagem criada
        """
        # Mapear nome da classe para a classe correspondente
        classes = {
            "Guerreiro": Guerreiro(),
            "Mago": Mago(),
            "Ladino": Ladino()
        }
        
        if classe_nome not in classes:
            raise ClasseInvalida(f"Classe '{classe_nome}' não encontrada")
            
        classe = classes[classe_nome]
        
        if len(habilidades) > classe.limite_habilidades:
            raise ClasseInvalida(f"Personagem {nome} excede o limite de habilidades para a classe {classe_nome}")
        
        habilidades_obj = []
        for hab_nome in habilidades:
            if hab_nome == "Bola de Fogo":
                habilidades_obj.append(BolaDeFogo("Uma bola de fogo que causa dano em área."))
            elif hab_nome == "Cura":
                habilidades_obj.append(Cura("Uma cura que recupera 10 pontos de vida."))
            elif hab_nome == "Tiro de Arco":
                habilidades_obj.append(TiroDeArco("Um tiro de arco que causa dano em área."))
            else:
                habilidades_obj.append(Habilidade(hab_nome, f"Habilidade {hab_nome}", 5))
        
        return Personagem(nome, classe, habilidades_obj)

    def __str__(self):
        inventario_str = ', '.join([hab.nome for hab in self.__inventario]) if self.__inventario else "Vazio"
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

    def usar_habilidade(self):
        """Método para usar uma habilidade (caso tenha)."""
        if self.__inventario and len(self.__inventario) > 0:
            habilidade = self.__inventario.pop(0)  
            return habilidade.usar()
        else:
            return "Nenhuma habilidade disponível!"

    def atacar(self, alvo):
        """Método para atacar um alvo."""
        if isinstance(alvo, Personagem):
            dano_base = self.__classe.pontos_ataque + self.__classe.dado_de_ataque.jogar()
            dano_final = max(0, dano_base - alvo.classe.pontos_defesa)
            alvo.classe._Classe__pontos_vida -= dano_final  
            return f'{self.__nome} atacou {alvo.nome} e causou {dano_final} de dano!'
        else:
            return "Alvo inválido!"
