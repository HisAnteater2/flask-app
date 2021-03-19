import operator
import pickle
from collections import OrderedDict
from copy import deepcopy

from flask import Flask, jsonify, request

# Data to serve with our API
try:
    # Getting back the objects:
	with open('data.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
		Users = pickle.load(f)
except EOFError:
	Users = {}

# creating a Flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/', methods = ['GET', 'POST'])
def home():
	global Users
	UserRanked = deepcopy(Users)
	for user in UserRanked:
		del UserRanked[user]['password']
	if(request.method == 'GET'):
		return jsonify(UserRanked)

@app.route('/user/<username>/<password>/<score>', methods = ['GET', 'POST'])
def update_user(username, password, score):
	global Users
	print(Users)
	print(type(Users))
	if (type(username)!=str):
		return jsonify({'action': 'failure'}), 400
	if username in Users:
		if Users[username]['password'] != password:
			return jsonify({'action': 'failure'}), 400
		if Users[username]['score'] >= int(score):
			return jsonify({'action': 'success'}), 200
	Users.update({username: {'score': int(score), 'password': password}})
	Users = OrderedDict(reversed((sorted(Users.items(), key=lambda item: item[1]['score']))))
	# Saving the objects:
	with open('data.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
		pickle.dump(Users, f)
	return jsonify({'action': 'success'}), 200



# driver function
if __name__ == '__main__':
    app.run(debug = True)
