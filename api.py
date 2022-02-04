from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    data = {
        "nama" : "bintang"
    }
    return jsonify(data)

if "__main__" == __name__:
    app.run(host="0.0.0.0", port=1000)