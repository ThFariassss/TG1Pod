from Personagem import *
from Habilidade import *
from Dado import *
from Arena import *
from Log import *

# Criando alguns dados e habilidades
d20 = Dado(20)
habilidade_fogo = Habilidade("Golpe de Fogo", "Golpe que causa dano de fogo", 15)

# Criando personagens
guerreiro = Personagem(nome="Guerreiro", pontos_vida=100, dado_de_ataque=d20, pontos_ataque=10, pontos_defesa=5, limite_habilidade=3, classe="Guerreiro", inventario=[habilidade_fogo])
mago = Personagem(nome="Mago", pontos_vida=80, dado_de_ataque=d20, pontos_ataque=8, pontos_defesa=4, limite_habilidade=3, classe="Mago", inventario=[habilidade_fogo])

# Criando arena e adicionando personagens
arena = Arena()
arena.adicionar_personagem(guerreiro)
arena.adicionar_personagem(mago)

# Realizando o combate
resultado = arena.combate()
print(resultado)
