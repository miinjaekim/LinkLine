# app/voice_agent/api.py

from flask import Flask, request, jsonify
from app.voice_agent.crewai_logic import run_crewai_response

app = Flask(__name__)

@app.route('/llm/chat/completions', methods=['POST'])
def vapi_compatible_endpoint():
    try:
        data = request.get_json()
        print("VAPI RECEIVED:", data)

        messages = data.get("messages", [])
        user_input = next((m["content"] for m in reversed(messages) if m["role"] == "user"), None)

        print("Extracted user input:", user_input)

        if not user_input:
            print("No user input found.")
            return jsonify({"error": "No user message provided"}), 400

        agent_response = run_crewai_response(user_input)
        print("CrewAI Response:", agent_response)

        return jsonify({
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": agent_response
                    }
                }
            ]
        })

    except Exception as e:
        print("Error handling request:", e)
        return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
