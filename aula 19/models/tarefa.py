class Tarefa:
    def __init__(self, id, descricao, concluida=False):
        self.id = id
        self.descricao = descricao
        self.concluida = concluida

# Simula um banco de dados em memória
tarefas_db = []
contador_id = 1

def listar_tarefas():
    return tarefas_db

def adicionar_tarefa(descricao):
    global contador_id
    nova = Tarefa(contador_id, descricao)
    tarefas_db.append(nova)
    contador_id += 1
    return nova

def concluir_tarefa(tarefa_id):
    for t in tarefas_db:
        if t.id == tarefa_id:
            t.concluida = True
            return True
    return False