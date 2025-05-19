# Este arquivo expõe as classes e funções principais do pacote

from .Classe import Classe, Guerreiro, Mago, Ladino
from .Personagem import Personagem
from .Habilidade import Habilidade, BolaDeFogo, Cura, TiroDeArco
from .Erros import NLadosInvalido, ClasseInvalida
from .Carregar import baixar_personagem, logar_erro, criar_personagem
from .Jogo import *  

__version__ = 'Open beta 1.0.0'
