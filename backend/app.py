from flask import Flask
from flask_cors import CORS
from routes.mot_routes import mot_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(mot_blueprint, url_prefix='/api')

if __name__ == "__main__":
    app.run(port=8000)
