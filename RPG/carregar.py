from .Classe import *
from .Personagem import *
from .Erros import *
from .Jogo import *
import csv

def logar_erro(arquivo_name, dado):
    with open(arquivo_name, mode='w', encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerows(dado)

def baixar_personagem(caminho_name):
    personagens = []
    erros = []

    try:
        with open(caminho_name, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        nome = None
        classe = None
        habilidades = []
        lendo_habilidades = False

        for linha in linhas:
            linha = linha.strip()
            
            if not linha or linha.startswith("## "):
                continue

            if linha.startswith("### "):  
                if nome and classe and habilidades:
                    try:
                        personagem = Personagem.logar_personag(nome, classe, habilidades[:5])
                        personagens.append(personagem)
                    except ClasseInvalida as e:
                        erros.append([f"Erro de classe inválida para {nome}: {str(e)}"])
                    except NLadosInvalido as e:
                        erros.append([f"Erro de dados inválidos para {nome}: {str(e)}"])
                    except Exception as e:
                        erros.append([f"Erro ao instanciar personagem {nome}: {str(e)}"])
                elif nome:
                    erros.append([f"Dados incompletos: nome={nome}, classe={classe}, habilidades={habilidades}"])
                
                nome = linha[4:].strip()
                classe = None
                habilidades = []
                lendo_habilidades = False

            elif linha.startswith("- **Classe**:"):
                classe = linha.split(":")[1].strip()
                lendo_habilidades = False

            elif linha.startswith("- **Habilidades**"):
                lendo_habilidades = True  

            elif lendo_habilidades and (linha.startswith("- ") or linha.startswith("  - ")):
                if linha.startswith("  - "):
                    habilidade = linha[4:].strip()
                else:
                    habilidade = linha[2:].strip()
                habilidades.append(habilidade)

        if nome and classe and habilidades:
            try:
                personagem = Personagem.logar_personag(nome, classe, habilidades[:5])
                personagens.append(personagem)
            except ClasseInvalida as e:
                erros.append([f"Erro de classe inválida para {nome}: {str(e)}"])
            except NLadosInvalido as e:
                erros.append([f"Erro de dados inválidos para {nome}: {str(e)}"])
            except Exception as e:
                erros.append([f"Erro ao instanciar personagem {nome}: {str(e)}"])
        elif nome:
            erros.append([f"Dados incompletos: nome={nome}, classe={classe}, habilidades={habilidades}"])

    except Exception as e:
        erros.append([f"Erro geral: {str(e)}"])

    return personagens, erros
