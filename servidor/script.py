from flask import Flask, request, jsonify

app = Flask(__name__)

data = {}

@app.route('/write',methods=['post'])
def write():
    data.update(request.json)
    return jsonify({'success':True})

@app.route('/read',methods=['post'])
def read():
    return jsonify({tag:data.get(tag,None) for tag in request.json})

if __name__=='__main__':
    app.run(host='0.0.0.0')