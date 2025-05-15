def registrar_log(mensagem):
    """Registrar mensagens de erro em um arquivo de log."""
    with open('erros.log', 'a') as file:
        file.write(mensagem + '\n')
