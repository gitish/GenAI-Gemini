from flask import Flask, request, jsonify
from google.cloud import aiplatform
import google.generativeai as genai
import os

# Initialize Flask app
app = Flask(__name__)

# Initialize AI Platform client
aiplatform.init(project='gen-lang-client-0578368562', location='europe-west2')

# Define endpoint for text generation
@app.route('/create_model', methods=['POST'])
def createModel():
    """Generates text using a GenAI model.

    Returns:
        JSON response containing the generated text.
    """

    # Get request data
    data = request.get_json()
    prompt = data.get('prompt')
    print("*******")
    print(prompt)
    print("*******")
    # Check if prompt is provided
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Load the GenAI model
    model = aiplatform.gapic.ModelServiceClient.create_model(
        parent='projects/gen-lang-client-0578368562/locations/europe-west2',
        model=aiplatform.gapic.Model(
            display_name='SHAIL_MODEL_TEST',
            endpoint='SHAIL_ENDPOINT_TEST',
            version_id='1.0.0',
        )
    )

    # Generate text using the model
    response = model.predict(
        instances=[{'text': prompt}]
    )

    # Extract generated text from response
    generated_text = response.predictions[0]['text']

    # Return generated text as JSON response
    return jsonify({'text': generated_text})

@app.route('/generate_text', methods=['GET'])
def generateDefaultText():

    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)


    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Give me python code to sort a list")
    print(response)
    return response.text

@app.route('/generate_text', methods=['POST'])
def generatePromptText():
    """Generates text using a GenAI model.

    Returns:
        JSON response containing the generated text.
    """

    # Get request data
    data = request.get_json()
    prompt = data.get('prompt')
    

    # Check if prompt is provided
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
