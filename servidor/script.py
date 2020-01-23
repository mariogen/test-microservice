from flask import Flask, request, jsonify

app = Flask(__name__)

data = {}

@app.route('/write')
def write():
    data.update(request.args.to_dict())
    return jsonify({'success':True})

@app.route('/read')
def read():
    return jsonify({tag:data.get(tag,None) for tag in request.args.getlist('tag')})

if __name__=='__main__':
    app.run(host='0.0.0.0')