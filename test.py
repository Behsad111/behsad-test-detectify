# Simulerad Python-serverkod med potentiell sårbarhet
from flask import Flask, request

app = Flask(__name__)

@app.route('/load_file')
def load_file():
    filename = request.args.get('file')  # Användarens input hämtas direkt
    # OPS! Ingen sanering av 'filename'!
    # Här skulle en Path Traversal-attack kunna ske: 
    # /load_file?file=../../etc/passwd
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
