from flask import Blueprint, jsonify, redirect, request, render_template
from database.classes import Usuario, Equipe, Partida
from admin.decorators import login_required

admin_bp = Blueprint('admin',__name__,template_folder='templates')

########################## HOME/ADMIN ###############################
@admin_bp.route('/')
@login_required
def admin():
    return render_template('/admin/admin.html')

########################## EQUIPES ###############################
@admin_bp.route('/equipes')
@login_required
def equipes():
    return render_template('/admin/equipes.html',
        time = Equipe.listar()
    )

########################## CRIAR EQUIPE ###############################
@admin_bp.route('/equipes/criar', methods=['GET', 'POST'])
@login_required
def equipes_criar():
    equipe = {}
    erros = []
    mensagem = "Equipe criada com sucesso!"
    if request.method == 'POST':
        equipe = request.form
        erros = Equipe.criar(
            equipe.get('nome'),
            equipe.get('sigla'),
            equipe.get('local')
        )

        if len(erros) == 0:
            return redirect('/admin/equipes')

    return render_template(
        'admin/equipes_form.html',
        equipe = equipe,
        titulo='Adicionar',
        erros = erros
    )

########################## ALTERAR EQUIPE ###############################
@admin_bp.route('/equipes/alterar/<sigla>', methods=['GET', 'POST'])
@login_required
def equipe_alterar(sigla):
    equipe = Equipe.obter(sigla)
    erros = []
    if request.method == 'POST':
        equipe = request.form
        erros = Equipe.alterar(
            equipe.get('nome'),
            equipe.get('sigla'),
            equipe.get('local'),
        )
        if len(erros) == 0:
            return redirect('/admin/equipes')

    return render_template(
        'admin/equipes_form.html',
        equipe=equipe,
        titulo=f'Alterar',
        erros=erros
    )

########################## REMOVER EQUIPE ###############################
@admin_bp.route('/equipes/remover/<sigla>', methods=['POST'])
@login_required
def equipes_remover(sigla):
    Equipe.remover(sigla)
    return redirect('/admin/equipes')

########################## VERIFICAR EQUIPE ###############################
@admin_bp.route('/equipes/verificar/<sigla>')
@login_required
def equipes_verificar(sigla):
    equipe = Equipe.obter(sigla)
    resultado = {}
    if not equipe:
        resultado['existe'] = False
    else:
        resultado['existe'] = True
        resultado['mensagem'] = f'Sigla {sigla} já em uso'
    return jsonify(resultado)

########################## PARTIDAS ###############################
@admin_bp.route('/partidas')
@login_required
def partidas():
    return render_template('/admin/partidas.html',
        partida=Partida.listar()
    )

########################## CRIAR PARTIDAS ###############################
@admin_bp.route('/partidas/criar', methods=['GET', 'POST'])
@login_required
def partidas_criar():
    partida = {}
    erros = []
    if request.method == 'POST':
        partida = request.form
        partida = Partida.criar(
            partida.get('timecasa'),
            partida.get('timefora'),
            partida.get('goltime1'),
            partida.get('goltime2')
        )
        if len(erros) == 0:
            return redirect('/admin/partidas')

    return render_template(
        'admin/partidas_form.html',
        partida=partida,
        titulo='Adicionar Partida',
        erros=erros
    )

########################## ALTERAR PARTIDAS ###############################
@admin_bp.route('/partidas/alterar/<sigla>', methods=['GET', 'POST'])
@login_required
def partidas_alterar(sigla):
    curso = Curso.obter(sigla)
    erros = []
    if request.method == 'POST':
        curso = request.form
        erros = Curso.alterar(
            partida.get('timecasa'),
            partida.get('timefora'),
            partida.get('goltime1'),
            partida.get('goltime2')
        )

        if len(erros) == 0:
            return redirect('/admin/equipes')

    return render_template(
        'admin/partidas_forms.html',
        curso=curso,
        titulo=f'Alterar {equipe.sigla}',
        erros=erros
    )

########################## REMOVER PARTIDAS ###############################
@admin_bp.route('/partidas/remover/<sigla>', methods=['POST'])
@login_required
def partidas_remover(sigla):
    Curso.remover(sigla)
    return redirect('/admin/partidas')

########################## VERIFICAR PARTIDAS ###############################
@admin_bp.route('/partidas/verificar/<sigla>')
@login_required
def partidas_verificar(sigla):
    partidas = Partida.obter(sigla)
    resultado = {}
    if not curso:
        resultado['existe'] = False
    else:
        resultado['existe'] = True
        resultado['mensagem'] = f'Sigla {sigla} já em uso'
    return jsonify(resultado)