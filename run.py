from flask import Flask, jsonify, request
from app.theory.scales import get_scale
from app.routes.swagger import swagger_bp, get_swagger_ui_blueprint

app = Flask(__name__)

swaggerui_blueprint = get_swagger_ui_blueprint()
app.register_blueprint(swagger_bp)
app.register_blueprint(swaggerui_blueprint)

GERMAN_TO_ENGLISH_NOTES = {
    "C": "C",
    "Cis": "C#",
    "Des": "Db",
    "D": "D",
    "Dis": "D#",
    "Es": "Eb",
    "E": "E",
    "F": "F",
    "Fis": "F#",
    "Ges": "Gb",
    "G": "G",
    "Gis": "G#",
    "As": "Ab",
    "A": "A",
    "Ais": "A#",
    "B": "Bb",
    "H": "B"
}

@app.route('/api/scales/<tonic>/<mode>')
def scale(tonic, mode):
    tonic = GERMAN_TO_ENGLISH_NOTES.get(tonic, tonic)
    mode = request.args.get('mode', mode)

    if not tonic or not mode:
        return jsonify({'error': 'Tonic and mode are required parameters.'}), 400
    try:
        scale_notes = get_scale(tonic, mode)
        return jsonify({'tonic': tonic, 'mode': mode, 'scale': scale_notes})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
if __name__ == "__main__":
    app.run(debug=True, port=3000)