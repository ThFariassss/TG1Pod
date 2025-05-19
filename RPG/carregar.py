from .Classe import *
from .Personagem import *
from .Erros import *
from .Jogo import *
from .Habilidade import *
import csv
import os

"""Função que devolve uma lista de erros."""
def logar_erro(arquivo_name, dado):
    with open(arquivo_name, mode='w', encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerows(dado)
"""Função que lê o arquivo e devolve uma lista de personagens."""
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

"""Função utilizada para criar um personagem, validando a classe e as habilidades, e adicionando ao arquivo markdown."""      
def criar_personagem(caminho_name, nome, classe_nome, habilidades_nomes):

    # Validar classe
    classes_validas = ["Guerreiro", "Mago", "Ladino"]
    if classe_nome not in classes_validas:
        return False, f"Classe inválida: {classe_nome}. Use uma das seguintes: {', '.join(classes_validas)}"
    
    # Validar habilidades
    habilidades_validas = ["Cura", "Tiro de Arco", "BolaDeFogo"]
    for hab in habilidades_nomes:
        if hab not in habilidades_validas:
            return False, f"Habilidade inválida: {hab}. Use uma das seguintes: {', '.join(habilidades_validas)}"
    
    # Verificar limite de habilidades por classe
    limite_habilidades = 5
    if classe_nome == "Guerreiro":
        limite_habilidades = 2
    elif classe_nome == "Mago":
        limite_habilidades = 5
    elif classe_nome == "Ladino":
        limite_habilidades = 3
        
    if len(habilidades_nomes) > limite_habilidades:
        return False, f"Personagem {nome} excede o limite de {limite_habilidades} habilidades para a classe {classe_nome}"
    
    try:
        # Tenta criar o personagem usando o método estático existente
        try:
            personagem = Personagem.logar_personag(nome, classe_nome, habilidades_nomes)
        except ClasseInvalida as e:
            return False, f"Erro de classe inválida: {str(e)}"
        except Exception as e:
            return False, f"Erro ao criar personagem: {str(e)}"
        
        # Formatar o personagem no formato Markdown usado no arquivo
        conteudo_personagem = formatar_personagem_markdown(nome, classe_nome, habilidades_nomes)
        
        # Verificar se o arquivo existe e criar se necessário
        if not os.path.exists(caminho_name):
            with open(caminho_name, 'w', encoding='utf-8') as arquivo:
                arquivo.write("## Personagens\n\n")
        
        # Adicionar o personagem ao arquivo
        with open(caminho_name, 'a', encoding='utf-8') as arquivo:
            arquivo.write(conteudo_personagem)
        
        return True, f"Personagem {nome} criado com sucesso!"
        
    except Exception as e:
        return False, f"Erro ao criar personagem: {str(e)}"
"""Função para sanear a entrada do usuário, e formatar o personagem em Markdown."""
def formatar_personagem_markdown(nome, classe_nome, habilidades):
   
    texto = f"\n### {nome}\n"
    texto += f"- **Classe**: {classe_nome}\n"
    texto += "- **Habilidades**:\n"
    
    for habilidade in habilidades:
        texto += f"  - {habilidade}\n"
        
    return texto
