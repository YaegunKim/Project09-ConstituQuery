from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import time
import os

openai.api_key = "your_key"

app = Flask(__name__, template_folder='templates')

CORS(app)


@app.route('/')
def index():
    return render_template('EthanGPT_General.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    print("Inside get-response route")   # Debug print
    data = request.get_json()
    print(f"Received data: {data}")      # Debug print
    prompt = data['prompt']
    response = get_completion(prompt)
    return jsonify({'response': response})

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.5,
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        return f"Error in generating response: {e}"



if __name__ == '__main__':
    app.run(port=5001, debug=True, use_reloader=False)

