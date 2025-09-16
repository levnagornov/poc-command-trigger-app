from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/exec", methods=["POST"])
def exec_cmd():
    cmd = request.json.get("cmd")
    if not cmd:
        return jsonify({"error": "no command"}), 400

    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        return jsonify({"output": result.decode("utf-8")})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output.decode("utf-8")}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
