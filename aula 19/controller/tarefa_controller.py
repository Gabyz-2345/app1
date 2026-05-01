from flask import Blueprint, render_template, request, redirect, url_for
from models.tarefa import listar_tarefas, adicionar_tarefa, concluir_tarefa

tarefa_bp = Blueprint('tarefa', __name__)

@tarefa_bp.route('/')
def index():
    tarefas = listar_tarefas()
    return render_template('index.html', tarefas=tarefas)

@tarefa_bp.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        if descricao:
            adicionar_tarefa(descricao)
        return redirect(url_for('tarefa.index'))
    return render_template('cadastrar.html')

@tarefa_bp.route('/concluir/<int:tarefa_id>')
def concluir(tarefa_id):
    concluir_tarefa(tarefa_id)
    return redirect(url_for('tarefa.index'))