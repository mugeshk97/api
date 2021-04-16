from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

_token = 'my'

def response(status, message, data):
    return(jsonify({"status":status,"message":message,"data":data}))

# decorator for checking token
def checkToken(func):
    @wraps(func)
    def check():
        try:
            token = request.headers['token']
            if token == _token:
                return func()
            else:
                return response("failure","unauthorized",{})
            
        except Exception as e:
            return response("failure",str(e),{})
    return check


@app.route('/', methods = ['GET'])
@checkToken
def index():
	data = {'name': 'Mugesh', 'designation': 'AI Engineer'}, {'name': 'Manoj', 'designation': 'UI Developer'}
	return jsonify(data)

@app.route('/food', methods=['POST'])
@checkToken
def food():
	df = request.get_json()
	return jsonify(df)

if __name__ == '__main__':
	app.run(debug=True)
