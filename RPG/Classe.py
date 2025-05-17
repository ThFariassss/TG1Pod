from abc import ABC, abstractmethod
from .Jogo import *
from .Erros import *

class Classe(ABC):
    def __init__(self, nome, pontos_vida, dado_de_ataque, pontos_de_ataque, pontos_defesa, limite_habilidades):
        self.__nome = nome
        self.__pontos_vida = pontos_vida
        self.__dado_de_ataque = dado_de_ataque
        self.__pontos_ataque = pontos_de_ataque
        self.__pontos_defesa = pontos_defesa
        self.__limite_habilidades = limite_habilidades

    def __str__(self):
        return (f"Nome: {self.__nome}, Pontos de Vida: {self.__pontos_vida}, " "Dado de Ataque: {self.__dado_de_ataque}, Pontos de Ataque: {self.__pontos_ataque}, " "Pontos de Defesa: {self.__pontos_defesa}, Limite de Habilidades: {self.__limite_habilidades}")

    def __repr__(self):
        return (f"Classe(nome='{self.__nome}', pontos_vida={self.__pontos_vida}, " "dado_de_ataque={self.__dado_de_ataque}, pontos_de_ataque={self.__pontos_ataque}, " "pontos_defesa={self.__pontos_defesa}, limite_habilidades={self.__limite_habilidades})")
    def __eq__(self, other):
        if isinstance(other, Classe):
            return self.__nome == other.__nome and \
                   self.__pontos_vida == other.__pontos_vida and \
                    self.__dado_de_ataque == other.__dado_de_ataque and \
                    self.__pontos_ataque == other.__pontos_ataque and \
                    self.__pontos_defesa == other.__pontos_defesa and \
                    self.__limite_habilidades == other.__limite_habilidades
        return False
    
    @property
    def dado_de_ataque(self):
        return self.__dado_de_ataque

    @dado_de_ataque.setter
    def dado_de_ataque(self, novo_dado):
        self.__dado_de_ataque = novo_dado

    @abstractmethod
    def atacar(self):
        """Método abstrato que será implementado por subclasses específicas (ex: Guerreiro, Mago)"""
        pass

    @property
    def nome(self):
        return self.__nome

    @property
    def pontos_vida(self):
        return self.__pontos_vida

    @property
    def pontos_ataque(self):
        return self.__pontos_ataque

    @property
    def pontos_defesa(self):
        return self.__pontos_defesa

    @property
    def limite_habilidades(self):
        return self.__limite_habilidades

class Guerreiro(Classe):
    def __init__(self):
        pontos_defesa = 8
        pontos_vida = 10 + (pontos_defesa * 5)
        dado_de_ataque = D12()
        pontos_ataque = 6
        limite_habilidades = 2
        super().__init__("Guerreiro", pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades)

    def atacar(self, alvo): 
        dano = self.dado_de_ataque.jogar() + self.pontos_ataque
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano!")

class Mago(Classe):
    def __init__(self):
        pontos_defesa = 3
        pontos_vida = 8 + (pontos_defesa * 2)
        dado_de_ataque = D6()
        pontos_ataque = 10
        limite_habilidades = 5
        super().__init__("Mago", pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades)

    def atacar(self, alvo): 
        dano = self.dado_de_ataque.jogar() + self.pontos_ataque
        print(f"{self.nome} lança uma magia em {alvo.nome} causando {dano} de dano!")

class Ladino(Classe):
    def __init__(self):
        pontos_defesa = 5
        pontos_vida = 6 + (pontos_defesa * 3)
        dado_de_ataque = D8()
        pontos_ataque = 8
        limite_habilidades = 3
        super().__init__("Ladino", pontos_vida, dado_de_ataque, pontos_ataque, pontos_defesa, limite_habilidades)

    def atacar(self, alvo): 
        dano = self.dado_de_ataque.jogar() + self.pontos_ataque
        print(f"{self.nome} golpeia {alvo.nome} nas sombras causando {dano} de dano!")