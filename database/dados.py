from classes import Equipe, Partida, Usuario

EQUIPES = [
    Equipe('Equipe 1', 'EQ1', 'São Paulo-SP'),
    Equipe('Equipe 2', 'EQ2', 'Rio de Janeiro-RJ'),
    Equipe('Equipe 3', 'EQ3', 'Minas Gerais-MG'),
    Equipe('Equipe 4', 'EQ4', 'Vitória-ES'),
    Equipe('Equipe 5', 'EQ5', 'Campinas-SP')
]
PARTIDAS = [
    Partida(EQUIPES[0], EQUIPES[1], 1, 0),
    Partida(EQUIPES[1], EQUIPES[0], 2, 5),
    Partida(EQUIPES[0], EQUIPES[2], 1, 3),
    Partida(EQUIPES[2], EQUIPES[0], 5, 3),
    Partida(EQUIPES[0], EQUIPES[3], 5, 2),
    Partida(EQUIPES[3], EQUIPES[0], 5, 3),
    Partida(EQUIPES[0], EQUIPES[4], 3, 5),
    Partida(EQUIPES[4], EQUIPES[0], 3, 1),
    Partida(EQUIPES[1], EQUIPES[2], 0, 0),
    Partida(EQUIPES[2], EQUIPES[1], 0, 0),
    Partida(EQUIPES[1], EQUIPES[3], 0, 0),
    Partida(EQUIPES[3], EQUIPES[1], 0, 0),
    Partida(EQUIPES[1], EQUIPES[4], 0, 0),
    Partida(EQUIPES[4], EQUIPES[1], 0, 0),
    Partida(EQUIPES[2], EQUIPES[3], 0, 0),
    Partida(EQUIPES[3], EQUIPES[2], 0, 0),
    Partida(EQUIPES[2], EQUIPES[4], 0, 0),
    Partida(EQUIPES[4], EQUIPES[2], 0, 0),
    Partida(EQUIPES[3], EQUIPES[4], 0, 0),
    Partida(EQUIPES[4], EQUIPES[3], 0, 0)
]
USUARIOS = [
    Usuario('admin@admin.com', 'admin123*')
]
