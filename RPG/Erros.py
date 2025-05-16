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