from flask import Flask, request, jsonify, render_template
import os
import ollama

# Get base path
base_path = os.path.dirname(os.path.abspath(__file__))

# Initialize Flask app and configure template/static folders
app = Flask(
    __name__,
    template_folder=os.path.join(base_path, '../templates'),
    static_folder=os.path.join(base_path, '../static')  # optional, only if CSS/JS are here
)

# Load information from the text file once
with open(os.path.join(base_path, 'informa.txt'), 'r') as f:
    context = f.read()

# Serve the frontend UI
@app.route('/')
def index():
    return render_template('index.html')

# Chat route to handle messages
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    print("📩 User asked:", user_input)

    prompt = f"Based on the following information:\n{context}\nAnswer this question: {user_input}"

    try:
        response = ollama.chat(model='llama3', messages=[
            {"role": "user", "content": prompt}
        ])
        reply = response['message']['content'].strip()
        return jsonify({"response": reply})
    except Exception as e:
        print("❌ LLaMA Error:", str(e))
        return jsonify({"response": "⚠️ Failed to generate response."})

if __name__ == '__main__':
    app.run(debug=True)
