# Arquivo __init__.py para o pacote RPG
# Este arquivo expõe as classes e funções principais do pacote

# Importações das classes principais
from .Classe import Classe, Guerreiro, Mago, Ladino
from .Personagem import Personagem
from .Habilidade import Habilidade, BolaDeFogo, Cura, TiroDeArco
from .Erros import NLadosInvalido, ClasseInvalida
from .Carregar import baixar_personagem, logar_erro
from .Jogo import *  # Importa as classes de dados e outras funcionalidades do jogo

# Versão do pacote
__version__ = '1.0.0'
