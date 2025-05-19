#Classe de erros, que define os erros que podem ocorrer no jogo.
class NLadosInvalido(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    def __str__(self): 
        return "NLadosInvalido: ("+ self.mensagem +")"
        
class ClasseInvalida(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
    def __str__(self):  
        return "ClasseInvalida: ("+ self.mensagem +")"
