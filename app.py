import os
from flask import Flask
from dotenv import load_dotenv
from src.config.iniciador import IniciadorApp

def crear_app():
    load_dotenv()
    
    app = Flask(__name__)
    IniciadorApp.configurar(app)
    
    return app

app = crear_app()

if __name__ == '__main__':
    puerto = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=puerto, debug=True)
