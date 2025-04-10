'''
python3 -m venv myenv
source myenv/bin/activate

pip3 install flask flask-cors openai

export OPENAI_API_KEY="your_key" # https://platform.openai.com/settings/organization/general
'''
from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


app = Flask(__name__)
CORS(app)  # Allow React frontend to communicate with Flask

# Function to interact with OpenAI GPT
def ask_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" if needed
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message.content

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    
    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400
    
    try:
        ai_response = ask_openai(user_message)
        return jsonify({"response": ai_response})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
