from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

def llm_model(question, data):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content(f'''You are an Friend and a AI assistant for Deepak PROVIDE THE PERFECT ANSWER IN THREE POINTS 
    for the user querstion from the available data!!\n" Question:{question} \n CONTEXT:{data}''')    
    return response.text

@app.route('/model', methods=['POST'])
def receive_input():
    # Get data sent from the other Flask application
    data = request.json
    user_question = data.get('user_question')
    response = data.get('response')
    out = llm_model(user_question, response)
    return jsonify({'output': out})

if __name__ == '__main__':
    app.run(debug=True)
