from abc import ABC, abstractmethod
import random

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
         raise ValueError("O número de lados deve ser maior que zero.")

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
