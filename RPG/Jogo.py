from abc import ABC, abstractmethod
import random
from .Erros import *

class Dado(ABC):
    """Classe base para dados."""
    def __init__(self, lados):
        self.__lados = lados

    def __str__(self):
        return f'Dado de {self.__lados} lados'

    def __repr__(self):
        return f'Dado(lados={self.__lados})'

    def __eq__(self, other):
        if isinstance(other, Dado):
            return self.__lados == other.__lados
        return False

    @abstractmethod
    def jogar(self):
        pass

    @property
    def lados(self):
        return self.__lados
    
    @lados.setter
    def lados(self, valor):
      if valor > 0:
         self.__lados = valor
      else:
         raise NLadosInvalido("O número de lados deve ser maior que zero.")

    def __lt__(self, other):
        if isinstance(other, Dado):
            return self.lados < other.lados
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Dado):
            return self.lados <= other.lados
     

    def __gt__(self, other):
        if isinstance(other, Dado):
            return self.lados > other.lados
    

    def __ge__(self, other):
     if isinstance(other, Dado):
            return self.lados >= other.lados
    

class D4(Dado):
    """Dado de 4 lados."""
    def __init__(self,):
        super().__init__(4)
    def jogar(self,):
        return random.randint(1, self.lados)
class D6(Dado):
    """Dado de 6 lados."""
    def __init__(self,):
        super().__init__(6)
    def jogar(self,):
        return random.randint(1, self.lados)  
class D8(Dado):
    """Dado de 8 lados."""
    def __init__(self,):
        super().__init__(8)
    def jogar(self,):
        return random.randint(1, self.lados)
class D10(Dado):
    """Dado de 10 lados."""
    def __init__(self,):
        super().__init__(10)
    def jogar(self,):
        return random.randint(1, self.lados)
class D12(Dado):
    """Dado de 12 lados."""
    def __init__(self,):
        super().__init__(12)
    def jogar(self,):
        return random.randint(1, self.lados)
class D20(Dado):
    """Dado de 20 lados."""
    def __init__(self,):
        super().__init__(20)

    def jogar(self,):
        return random.randint(1, self.lados)


class Arena:
    def __init__(self):
        self.personagens = []

    def adicionar_personagem(self, personagem):
        self.personagens.append(personagem)

    def remover_personagem(self, personagem):
        if personagem in self.personagens:
            self.personagens.remove(personagem)
            return True
        return False

    def combate(self):
        if len(self.personagens) < 2:
            return "É necessário pelo menos dois personagens para iniciar o combate."

        dado = Dado(20)  
        vivos = self.personagens.copy()

        turno = 0
        while len(vivos) > 1:
            atacante = vivos[turno % len(vivos)]
            alvos = [p for p in vivos if p != atacante]
            defensor = random.choice(alvos)

            ataque_rodada = dado.jogar() + atacante.classe.pontos_ataque

            if ataque_rodada > defensor.classe.pontos_defesa:
                dano = atacante.classe.pontos_ataque
                defensor.classe._Classe__pontos_vida -= dano

                print(f"{atacante.nome} ataca {defensor.nome} com sucesso! Dano: {dano}. PV restante de {defensor.nome}: {defensor.classe.pontos_vida}")
                
                if defensor.classe.pontos_vida <= 0:
                    print(f"{defensor.nome} foi derrotado!")
                    vivos.remove(defensor)
            else:
                print(f"{atacante.nome} atacou {defensor.nome} e errou!")

            turno += 1

        vencedor = vivos[0]
        print(f"Combate encerrado! Vencedor: {vencedor.nome}")
        return vencedor
