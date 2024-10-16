import openai
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set the Azure OpenAI API key and endpoint from the environment variables
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

# Azure-specific API version (change if necessary)
api_version = "2023-06-01-preview"

# Function to interact with Azure OpenAI (using your specified deployment name)
def generate_response(prompt, model="Mybot-gpt-4o"):  # Use your deployment name here
    try:
        # Call the Azure OpenAI API
        response = openai.ChatCompletion.create(
            engine=model,  # Use the deployment name for the engine
            messages=[
                {"role": "system", "content": """
                You are a software development assistant. You can write Python, JavaScript, or Java code. You help debug code and suggest tests.
                If a user asks for code, provide a full example.
                If a user provides code, suggest improvements or fix errors.
                If a user asks for a test, create unit test examples.
                """},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500,
            temperature=0.7,
            api_base=azure_openai_endpoint,
            api_type="azure",
            api_version=api_version
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Flask route to render the chatbot page
@app.route('/')
def index():
    return render_template('index.html')

# Route to process user input
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = generate_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
