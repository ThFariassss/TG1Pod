# Carregar.py

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
        with open(caminho_name, 'r', encoding='utf-8') as gerador:
            pasta = gerador.read()
            blocos = pasta.strip().split('\n\n')  # <-- corrige para usar .strip()

            for bloco in blocos:
                linhas = bloco.strip().split('\n')  # <-- corrigido aqui: bloco, não blocos
                nome = None
                classe = None
                inventarios = []

                for linha in linhas:
                    linha = linha.strip()
                         
                    if linha.startswith('###'):
                        nome = linha[4:].strip()
                        print(f"Nome: {nome} ")

                    elif linha.startswith('- **Classe**:'):
                        classe = linha.split(':')[1].strip()
                        
                    elif linha.startswith('**Habilidades**'):
                        inventarios = linha.split(':')[1].strip().split(',')

                if nome and classe and inventarios:
                    try:
                        personagem = Personagem.logar_personag(nome, classe, inventarios[:5])
                        personagens.append(personagem)
                    except Exception as e:
                        erros.append([f"Erro ao instanciar personagem {nome}: {str(e)}"])
                else:
                    erros.append([f"Dados incompletos: nome={nome}, classe={classe}, inventarios={inventarios}"])

    except NLadosInvalido as e:
        erros.append([f"Erro de dados de dado: {str(e)}"])

    except ClasseInvalida as e:
        erros.append([f"Classe inválida: {str(e)}"])
    print(f"Personagens:", personagens)
    return personagens, erros
