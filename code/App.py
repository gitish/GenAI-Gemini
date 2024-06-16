from flask import Flask, request, jsonify
from google.cloud import aiplatform

# Initialize Flask app
app = Flask(__name__)

# Initialize AI Platform client
aiplatform.init(project='YOUR_PROJECT_ID', location='YOUR_REGION')

# Define endpoint for text generation
@app.route('/generate_text', methods=['POST'])
def generate_text():
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

    # Load the GenAI model
    model = aiplatform.gapic.ModelServiceClient.create_model(
        parent='projects/YOUR_PROJECT_ID/locations/YOUR_REGION',
        model=aiplatform.gapic.Model(
            display_name='YOUR_MODEL_NAME',
            endpoint='YOUR_ENDPOINT_NAME',
            version_id='YOUR_VERSION_ID',
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

if __name__ == '__main__':
    app.run(debug=True)
