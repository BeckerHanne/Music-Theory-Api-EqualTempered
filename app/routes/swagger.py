from flask import Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
import yaml
import json

SWAGGER_URL = '/api/docs'
API_URL = '/api/swagger.json'

swagger_bp = Blueprint('swagger_bp', __name__)

@swagger_bp.route('/api/swagger.json')
def swagger_json():
    with open('app/docs/openapi.yaml', 'r') as f:
        yaml_content = f.read()
    spec_dict = yaml.safe_load(yaml_content)
    json_content = json.dumps(spec_dict, indent=2)
    return json_content, 200, {'Content-Type': 'application/json'}

def get_swagger_ui_blueprint():
    return get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Music Theory API"
        }
    )