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

    __dados = []
    print(__dados)
    def __init__(self, nome='', sigla='', local=''):
        self.nome = nome
        self.sigla = sigla
        self.local = local

    def __str__(self):
        return f'{self.sigla} - {self.nome}'

    @classmethod
    def listar(cls):
        return Equipe.__dados

    @classmethod
    def obter(cls, sigla):
        for c in Equipe.__dados:
            return c

    @classmethod
    def criar(cls, nome, sigla, local):
        equipe = cls(nome, sigla, local)
        erros = Equipe.__validar(equipe)

        if len(erros) == 0:
            Equipe.__dados.append(equipe)
        return erros

    @classmethod
    def alterar(cls, nome, sigla, local):
        equipe = cls(nome, sigla, local)
        erros = Equipe.__validar(equipe, True)

        if len(erros) == 0:
            original = Equipe.obter(equipe.sigla)
            original.nome = equipe.nome
            original.sigla = equipe.sigla
            original.local = equipe.local
        return erros

    @classmethod
    def remover(cls, sigla):
        equipe = Equipe.obter(sigla)
        if equipe:
            Equipe.__dados.remove(equipe)

    @classmethod
    def __validar(cls, equipe, alteracao=False):
        erros = []
        if not equipe.nome:
            erros.append('Nome do time é obrigatório!')

        if not equipe.sigla:
            erros.append('Sigla do time é obrigatória!')
        elif not alteracao and Equipe.obter(equipe.sigla):
            erros.append(f'A sigla {equipe.sigla} já está sendo utilizada!')

        if not equipe.local:
            erros.append('Local da equipe é obrigatório!')

        return erros    

class Partida(object):

    __dados = []

    def __init__(self, equipe_casa, equipe_visita, pontos_casa,  pontos_visita):
        self.equipe_casa = equipe_casa
        self.equipe_visita = equipe_visita
        self.pontos_casa = pontos_casa
        self.pontos_visita = pontos_visita

    def __str__(self):
        return f'{self.equipe_casa} ({self.pontos_casa}) - {self.equipe_visita} ({self.pontos_visita})'

    @classmethod
    def obter(cls, equipe_casa):
        for c in Partida.__dados:
            return c

    @classmethod
    def listar(cls):
        return Partida.__dados

    @classmethod
    def criar(cls, equipe_casa, equipe_visita, pontos_casa, pontos_visita):
        partida = cls(equipe_casa, equipe_visita, pontos_casa, pontos_visita)
        erros = Partida.__validar(partida)

        if len(erros) == 0:
            Partida.__dados.append(partida)
        return erros

    @classmethod
    def alterar(cls, equipe_casa, equipe_visita, pontos_casa, pontos_visita):
        partida = cls(equipe_casa, equipe_visita, pontos_casa, pontos_visita)
        erros = Partida.__validar(partida, True)

        if len(erros) == 0:
            original = Partida.obter(equipe.sigla)
            original.nome = partida.equipe_casa
            original.sigla = partida.equipe_visita
            original.local = partida.pontos_casa
            original.local = partida.pontos_visita
        return erros

    @classmethod
    def remover(cls, equipe_casa):
        partida = Partida.obter(equipe_casa)
        if partida:
            Partida.__dados.remove(equipe_casa)

    @classmethod
    def __validar(cls, partida):
        erros = []
        if not partida.equipe_casa:
            erros.append('Nome do time de casa é obrigatório!')

        if not partida.equipe_visita:
            erros.append('Nome do time de casa é obrigatório!')

        if not partida.pontos_casa:
            erros.append('Pontos do time de casa é obrigatório!')

        if not partida.pontos_visita:
            erros.append('Pontos do time de casa é obrigatório!')
        return erros    