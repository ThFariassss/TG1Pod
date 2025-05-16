class Log:
    @staticmethod
    def registrar(mensagem: str, arquivo='erros.log'):
        try:
            with open(arquivo, 'a', encoding='utf-8') as file:
                file.write(mensagem + '\n')
        except Exception as e:
            print(f"Erro ao registrar log: {e}")
#Log.registrar("mensagem de erro")
