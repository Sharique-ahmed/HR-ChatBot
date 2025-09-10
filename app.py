from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from agentConfig import hr_agent

app = Flask(__name__)
CORS(app)  # enable CORS if needed

# ---------------------------
# Routes
# ---------------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    print("The input is -->", user_message)

    # Pass user input to HR Agent
    response = hr_agent.invoke({"input": user_message})
    reply = response.get("output", str(response))

    return jsonify({"reply": reply})


# ---------------------------
# Run server
# ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
