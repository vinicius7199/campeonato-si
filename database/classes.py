class Usuario(object):

    __dados = []

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def __str__(self):
        return f'{self.usuario}'
    
    @classmethod
    def autenticar(cls, usuario, senha):
        usuario = Usuario.obter(usuario)
        if usuario and usuario.senha == senha:
            return usuario
            
    @classmethod
    def criar(cls, usuario, senha):
        Usuario.__dados.append(cls(usuario, senha))

    @classmethod
    def obter(cls, usuario):
        for u in Usuario.__dados:
            if u.usuario == usuario:
                return u

class Equipe(object):

    def __init__(self, nome='', sigla='', local=''):
        self.nome = nome
        self.sigla = sigla
        self.local = local

    def __str__(self):
        return f'{self.nome} ({self.sigla})'

class Partida(object):

    def __init__(self, equipe_casa, equipe_visita, pontos_casa,  pontos_visita):
        self.equipe_casa = equipe_casa
        self.equipe_visita = equipe_visita
        self.pontos_casa = pontos_casa
        self.pontos_visita = pontos_visita

    def __str__(self):
        return f'{self.equipe_casa} ({self.pontos_casa}) - {self.equipe_visita} ({self.pontos_visita})'
