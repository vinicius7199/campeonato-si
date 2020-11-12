import json
import os

from database.classes import Usuario

def carregar_dados(base_dir):
    with open(os.path.join(base_dir, 'dados.json')) as json_arq:
        dados = json.load(json_arq)
        carregar_usuarios(dados['usuarios'])


def carregar_usuarios(usuarios):
    for usuario in usuarios:
        Usuario.criar(
            usuario['usuario'],
            usuario['senha']
        )
    print(f'Carregados {len(usuarios)} usuários com sucesso!')


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    carregar_dados(base_dir)
