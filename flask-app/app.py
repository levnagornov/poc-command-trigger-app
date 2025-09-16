from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run():
    cmd = request.json.get("cmd")
    if not cmd:
        return jsonify({"error": "no command"}), 400

    try:
        # шлём команду в ubuntu API
        resp = requests.post("http://ubuntu:6000/exec", json={"cmd": cmd})
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
