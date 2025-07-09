from flask import Flask
from flask_cors import CORS
from routes.grab_mot_route import mot_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(mot_blueprint, url_prefix='/api')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
