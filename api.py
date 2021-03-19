import operator
from flask import Flask, jsonify, request
import pickle

# Data to serve with our API
try:
    # Getting back the objects:
	with open('data.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
		Users = pickle.load(f)
except EOFError:
	Users = {}

# creating a Flask app
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	global Users
	if(request.method == 'GET'):
		return jsonify(Users)

@app.route('/user/<username>/<score>', methods = ['GET', 'POST'])
def update_user(username, score):
	global Users
	if(request.method == 'GET'):
		if (type(username)!=str):
			return jsonify({'action': 'failure'}), 400
		if username in Users:
			if Users[username] >= int(score):
				return jsonify({'action': 'success'}), 200
		Users.update({username: int(score)})
		Users = dict(reversed((sorted(Users.items(), key=lambda item: item[1]))))
		# Saving the objects:
		with open('data.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
			pickle.dump(Users, f)
		return jsonify({'action': 'success'}), 200
	if(request.method == 'POST'):
		if (type(username)!=str):
			return jsonify({'action': 'failure'}), 400
		if username in Users:
			if Users[username] >= int(score):
				return jsonify({'action': 'success'}), 200
		Users.update({username: int(score)})
		Users = dict(reversed((sorted(Users.items(), key=lambda item: item[1]))))
		# Saving the objects:
		with open('data.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
			pickle.dump(Users, f)
		return jsonify({'action': 'success'}), 200


# driver function
if __name__ == '__main__':
    app.run(debug = True)
