from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    a = jsonify(request.get_json(force=True))
    print(request.get_json(force=True))
    return a

if __name__ == '__main__':
    app.run(debug=True)
