from flask_cors import CORS

def configurar_cors(app):
    CORS(app,
         resources={r"/api/*": {"origins": "*"}},
         supports_credentials=True,
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         allow_headers=["Content-Type", "Authorization", "X-Requested-With"]
    )
