import model

def adcionar_nota(texto):
    if texto.strip():
        model.salvar_banco(texto)
        return True
    return False 

def listar_notas():
    return model.ler_do_banco()

