import random
from Dado import Dado

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
