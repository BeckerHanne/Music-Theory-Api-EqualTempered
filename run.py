from flask import Flask, jsonify, request, send_from_directory
from flask.json.provider import DefaultJSONProvider
from app.theory.scales import get_scale
from app.theory.intervals import get_interval
from app.theory.chords import get_triad, get_seventh
from app.theory.diatonic import get_diatonic_chords
from app.routes.swagger import swagger_bp, get_swagger_ui_blueprint

class OrderedJSONProvider(DefaultJSONProvider):
    sort_keys = False  # Disable sorting of keys in JSON output

app = Flask(__name__)
app.json_provider_class = OrderedJSONProvider
app.json = OrderedJSONProvider(app)  # Initialize the custom JSON provider 

swaggerui_blueprint = get_swagger_ui_blueprint()
app.register_blueprint(swagger_bp)
app.register_blueprint(swaggerui_blueprint)

# ── Frontend static serving ──────────────────────────────────
@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:filename>')
def frontend_files(filename):
    return send_from_directory('frontend', filename)


GERMAN_TO_ENGLISH_NOTES = {
    "C": "C",
    "Ces": "Cb",
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

@app.route('/api/intervals/<note1>/<note2>')
def interval(note1, note2):
    note1 = GERMAN_TO_ENGLISH_NOTES.get(note1, note1)
    note2 = GERMAN_TO_ENGLISH_NOTES.get(note2, note2)

    if not note1 or not note2:
        return jsonify({'error': 'Two notes are required.'}), 400
    try:
        result = get_interval(note1, note2)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/chords/triads/<root>/<quality>')
def triad(root, quality):
    root = GERMAN_TO_ENGLISH_NOTES.get(root, root)
    inversion = request.args.get('inversion', 0, type=int)

    try:
        result = get_triad(root, quality, inversion=inversion)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/chords/seventh/<root>/<quality>')
def seventh(root, quality):
    root = GERMAN_TO_ENGLISH_NOTES.get(root, root)
    inversion = request.args.get('inversion', 0, type=int)

    try:
        result = get_seventh(root, quality, inversion=inversion)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/key/<tonic>/<mode>/chords')
def diatonic_chords(tonic, mode):
    tonic = GERMAN_TO_ENGLISH_NOTES.get(tonic, tonic)
    try:
        result = get_diatonic_chords(tonic, mode)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=3000)