import os
from flask import Flask
from database.carregador import carregar_dados
from website.controllers import site_bp

app = Flask(__name__)
app.secret_key = 'DOKASKDSAOAKA'

app.register_blueprint(site_bp)


if __name__ == '__main__':
    carregar_dados(
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)
            ),
            'database'
        )
    )
    app.run(
        debug=True
    )