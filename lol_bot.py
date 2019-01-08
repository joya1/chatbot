# Import flask with the request object
from flask import Flask, request, jsonify

# Create the web server
app = Flask(__name__)

# You can message lol_bot via <your website>/lol
@app.route('/lol', methods=['GET', 'POST'])
def lol_bot():
    # Get the value of the 'text' query parameter
    # request.args is a dictionary (cool!)
    text = request.values.get('text')
    return jsonify({
        'response_type': 'in_channel',
        'text': f'lol {text}',
    })

@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
  return jsonify({
    'version': '0.1',
    'response': {
      'outputSpeech': {
        'type': 'PlainText',
        'text': 'Hello, welcome to my bot'
      }
    }
  })    

if __name__ == '__main__':
    # Start the web server!
    app.run()

