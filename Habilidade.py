from .Classe import *
from .Dado import *
class Habilidade:
    def __init__(self, nome, descricao, pontos_ataque):
        super().__init__(nome, pontos_ataque)
        self.__descricao = descricao
    def __str__(self,):
        return f'Habilidade: {self.__nome}\n' \
               f'Descrição: {self.__descricao}\n' \
               f'Ataque: {self.__pontos_ataque}'
    def __eq__(self, other):
        if isinstance(other, Habilidade):
            return self.__nome == other.__nome and \
                   self.__descricao == other.__descricao and \
                   self.__pontos_ataque == other.__pontos_ataque
        return False   
    def __repr__(self):
        return f'Habilidade(nome={self.__nome}, descricao={self.__descricao}, pontos_ataque={self.__pontos_ataque})'
    @property   
    def nome(self):
        return self.__nome
    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, nova_descricao):
        self.__descricao = nova_descricao
    @property
    def pontos_ataque(self):
        return self.__pontos_ataque
    @pontos_ataque.setter
    def pontos_ataque(self, novo_pontos_ataque):
        self.__pontos_ataque = novo_pontos_ataque
    
    def usar(self,):
        """Método para usar a habilidade."""
        return f'Habilidade {self.__nome} usada! \n' \
                f'Descrição: {self.__descricao} \n' \
                f'Ataque: {self.__pontos_ataque}'
    
class BolaDeFogo(Habilidade):
    def __init__(self, descricao):
        super().__init__('Bola de Fogo', descricao, 10)
    def usar(self):
        return super().usar()
class Cura(Habilidade):
    def __init__(self, descricao):
        super().__init__('Cura', descricao, 10)
    def usar(self):
        return super().usar()
    
class TiroDeArco(Habilidade):
    def __init__(self, descricao):
        super().__init__('Tiro de Arco', descricao, 6)
    def usar(self):
        return super().usar()