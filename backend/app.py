from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
from routes.grab_mot_route import mot_blueprint
import subprocess

app = Flask(__name__)
CORS(app)

# Register MOT data blueprint
app.register_blueprint(mot_blueprint, url_prefix='/api')

# Ollama model endpoints
MODEL_NAME = "llama3.2"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    prompt = data.get('message', '')
    try:
        # Ollama CLI expects the prompt as a positional argument, not a flag
        result = subprocess.run(
            ['ollama', 'run', MODEL_NAME, prompt],
            capture_output=True, text=True, check=True
        )
        reply = result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return jsonify({
            'error': 'Ollama CLI error',
            'details': e.stderr.strip()
        }), 500
    return jsonify({'response': reply})

@app.route('/api/chat/stream', methods=['POST'])
def chat_stream():
    data = request.get_json() or {}
    prompt = data.get('message', '')
    # Use --stream before the prompt
    proc = subprocess.Popen(
        ['ollama', 'run', MODEL_NAME, '--stream', prompt],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    def generate():
        for line in proc.stdout:
            yield f"data: {line.strip()}\n\n"
        err = proc.stderr.read()
        if err:
            yield f"data: [ERROR] {err.strip()}\n\n"

    return Response(stream_with_context(generate()), mimetype='text/event-stream')

if __name__ == '__main__':
    print("Starting Flask app on http://0.0.0.0:8000...")
    @app.route('/')
    def home():
        return "Flask app is running!"

    app.run(host='0.0.0.0', port=8000, debug=True)