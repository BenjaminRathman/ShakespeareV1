from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)
CORS(app)  # This allows the frontend to make requests to this server

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/user_interface_files/<path:path>')
def serve_files(path):
    return send_from_directory('user_interface_files', path)

@app.route('/start-story', methods=['POST'])
def start_story():
    try:
        # Import and run your story code here
        from StoryTellerEngine.claude_interface import get_claude_response
        get_claude_response()
        
        return jsonify({
            'success': True,
            'message': 'Story started successfully!'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error starting story: {str(e)}'
        }), 500

if __name__ == '__main__':
    print("Server starting... Open http://localhost:5000 in your browser")
    app.run(debug=True) 