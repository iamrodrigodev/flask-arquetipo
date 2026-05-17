from flask import Flask
from src.controller.autenticacion_controller import autenticacion_bp
from src.controller.usuario_controller import usuario_bp
from src.controller.salud_controller import salud_bp

def registrar_rutas(app: Flask):
    """Registra todos los blueprints (rutas) de la aplicación."""
    app.register_blueprint(autenticacion_bp, url_prefix='/api/autenticacion')
    app.register_blueprint(usuario_bp, url_prefix='/api/usuario')
    app.register_blueprint(salud_bp, url_prefix='/api/salud')
