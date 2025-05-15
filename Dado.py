from abc import ABC, abstractmethod
import random
class Dado:
    def __init__(self,lados, ):
        self.__lados = lados
    def __str__(self,):
        return f'Dado de {self.__lados} lados'
    def __repr__(self):
        return f'Dado(lados={self.__lados})'
    def __eq__(self, other):    
        if isinstance(other, Dado):
            return self.__lados == other.__lados
        return False
    @abstractmethod
    def jogar(self):
        return random.randint(1, self.__lados)
    def get_lados(self):
        return self.__lados
    
    def __repr__(self):
        pass
class D4(Dado):
    pass
class D6(Dado):
    pass
class D8(Dado):
    pass
class D10(Dado):
    pass
class D12(Dado):
    pass
class D20(Dado):
    pass
