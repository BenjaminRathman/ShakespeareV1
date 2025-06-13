from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web_handler.story_web_handler import StoryWebHandler

app = Flask(__name__)
CORS(app)  # This allows the frontend to make requests to this server

# Create a single instance of the story handler
story_handler = StoryWebHandler()

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/user_interface_files/<path:path>')
def serve_files(path):
    return send_from_directory('user_interface_files', path)

@app.route('/start-story', methods=['POST'])
def start_story():
    try:
        result = story_handler.start_story()
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error starting story: {str(e)}'
        }), 500

@app.route('/continue-story', methods=['POST'])
def continue_story():
    try:
        data = request.get_json()
        user_input = data.get('input')
        
        if not user_input:
            return jsonify({
                'success': False,
                'message': 'No input provided'
            }), 400

        result = story_handler.continue_story(user_input)
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error continuing story: {str(e)}'
        }), 500

if __name__ == '__main__':
    print("Server starting... Open http://localhost:5000 in your browser")
    app.run(debug=True) 