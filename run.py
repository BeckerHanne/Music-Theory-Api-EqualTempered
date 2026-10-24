from flask import Flask, jsonify
from app.theory.scales import get_scale

app = Flask(__name__)

@app.route('/scale/<tonic>/<mode>')
def scale(tonic, mode):
    try:
        scale_notes = get_scale(tonic, mode)
        return jsonify({'tonic': tonic, 'mode': mode, 'scale': scale_notes})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
if __name__ == "__main__":
    app.run(debug=True, port=3000)