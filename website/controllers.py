from datetime import datetime
from database.classes import Usuario
from database.dados import EQUIPES
from flask import Blueprint, flash, redirect, render_template, request, session

site_bp = Blueprint(
    'website',
    __name__,
    template_folder='templates'
)


@site_bp.route('/')
def index():
    return render_template('index.html')

@site_bp.route('/time/<sigla>')
def time(sigla):
    siglas = EQUIPES[0]
    return render_template('time.html',
    sigla = siglas
    )

@site_bp.route('/entrar')
def entrar():
    return render_template('entrar.html')

@site_bp.route('/autenticar', methods=['POST'])
def autenticar():
    form = request.form
    usuario = Usuario.autenticar(
        form.get('usuario'),
        form.get('senha')
    )
    if usuario:
        session['usuario'] = usuario.usuario
        session['data'] = datetime.now().__str__()
        return redirect('/admin')
    else:
        erro = "Usuário ou senha inválidos"
        return render_template('entrar.html',
        mensagem = erro)

@site_bp.route('/sobre')
def sobre():
    return render_template('sobre.html')

@site_bp.route('/sair')
def sair():
    session.clear()
    erro = "Logout efetuado com sucesso!"
    return render_template('entrar.html',
    mensagem = erro)