from Classe import *
from Dado import *
class Personagem:
    qntd_instancias = 0
    def __init__(self, nome,pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa,limite_habilidade,classe, inventario):
        super().__init__(nome, pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidade)
        self.__inventario = inventario
        self.__classe = classe
        Personagem.qtd_instancias += 1        
    def __str__(self,):
        inventario_str = ', '.join(self.__inventario) if self.__inventario else "Vazio"
        return (f'Personagem: {self.__classe}\n'  
                f'Pontos de Vida: {self.pontos_vida}\n' 
                f'Ataque: {self.pontos_ataque}\n'
                f'Defesa: {self.pontos_defesa}\n'
                f'Inventário: {inventario_str}')
    
    def __repr__(self):
        return (f'Personagem(nome={self.nome}, pontos_vida={self.pontos_vida}, '
                f'dado_de_ataque={self.dado_de_ataque}, pontos_ataque={self.pontos_ataque}, '
                f'pontos_defesa={self.pontos_defesa}, limite_habilidade={self.limite_habilidade}, '
                f'classe={self.__classe}, inventario={self.__inventario})')
    def __eq__(self, other):
        if isinstance(other, Personagem):
            return self.nome == other.nome and \
                   self.pontos_vida == other.pontos_vida and \
                   self.dado_de_ataque == other.dado_de_ataque and \
                   self.pontos_ataque == other.pontos_ataque and \
                   self.pontos_defesa == other.pontos_defesa and \
                   self.limite_habilidade == other.limite_habilidade and \
                   self.__classe == other.__classe and \
                   self.__inventario == other.__inventario
        return False
    @property
    def inventario(self):
        return self.__inventario
    @inventario.setter      
    def inventario(self, novo_inventario):
        self.__inventario = novo_inventario
    @property   
    def classe(self):
        return self.__classe
    @classe.setter
    def classe(self, nova_classe):
        self.__classe = nova_classe
    @property
    def alvo(self):
        return self.__alvo
    @alvo.setter
    def alvo(self, novo_alvo):
        self.__alvo = novo_alvo
    @property
    def pontos_vida(self):
        return self.__pontos_vida
    @pontos_vida.setter
    def pontos_vida(self, novo_pontos_vida):
        self.__pontos_vida = novo_pontos_vida
    @property
    def dado_de_ataque(self):
        return self.__dado_de_ataque
    @dado_de_ataque.setter
    def dado_de_ataque(self, novo_dado_de_ataque):
        self.__dado_de_ataque = novo_dado_de_ataque
    @property
    def pontos_ataque(self):
        return self.__pontos_ataque
    @pontos_ataque.setter
    def pontos_ataque(self, novo_pontos_ataque):
        self.__pontos_ataque = novo_pontos_ataque
    @property
    def pontos_defesa(self):
        return self.__pontos_defesa
    @pontos_defesa.setter
    def pontos_defesa(self, novo_pontos_defesa):
        self.__pontos_defesa = novo_pontos_defesa
    @property
    def limite_habilidade(self):
        return self.__limite_habilidade
    @limite_habilidade.setter
    def limite_habilidade(self, novo_limite_habilidade):
        self.__limite_habilidade = novo_limite_habilidade
        
    def atacar(self, alvo):
        """Método para atacar um alvo."""
        if isinstance(alvo, Personagem):
            dano = self.pontos_ataque - alvo.pontos_defesa
            if dano < 0:
                dano = 0
            alvo.pontos_vida -= dano
            return f'{self.nome} atacou {alvo.nome} e causou {dano} de dano!'
        else:
            return "Alvo inválido!"
        
    def usar_habilidade(self,):
        """Método para usar uma habilidade."""
        if self.__habilidade:
            return self.__habilidade.usar()
        else:
            return "Nenhuma habilidade disponível!"
    
        

