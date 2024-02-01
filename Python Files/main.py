from flask import Flask, request, jsonify
import requests
import subprocess
import os
import json
import socket
import getpass


app = Flask(__name__)


# can use the following methods for dynamic routing
# use this to get server/machine name:
machine_name = socket.gethostname()
# use this to get username:
user_name = getpass.getuser()


@app.route('/manual_kickoff', methods=['POST'])
def external_hook():
	try:
		data = request.get_json()
		print(data)
		username = data.get('Username')
		server_name = data.get('Server Name')

		print(f'{server_name} run with {username}')

		# returns response and success code back to delegation webhook
		return jsonify(f'{server_name} - {username} reached external'), 200
	except Exception as e:
		return f'external Error: {str(e)}', 500


if __name__ == '__main__':
	app.run(debug=True, port=3000)
