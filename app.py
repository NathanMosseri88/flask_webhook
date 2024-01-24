from flask import Flask, request, jsonify
import requests
import subprocess
import os
import json
from cryptography.fernet import Fernet

app = Flask(__name__)


def get_secrets():
	with open('secrets.json') as secrets_file:
		secrets = json.load(secrets_file)

		return secrets


WHITE_LIST = get_secrets().get('whitelisted_IPs')


# when this endpoint is hit...
@app.route('/webhook', methods=['POST'])
def webhook():  # run this function.
	try:
		data = request.get_json()  # get the json body from request
		# file = data.get('file')  # get the value of the key named file
		requesting_ip = data.get('ip')
		if requesting_ip in WHITE_LIST:  # check if IP address in request is whitelisted

			servers = data.get('servers')  # list of server/username dicts
			print(servers)

			for server in servers:  # for each dict...
				external_webhook_url = f'https://exampleExternalUrl.com/{server["Server Name"]}'  # uniform request URL with dynamic endpoint
				payload = server  # request body with 'Server Name' and 'Username' dict
				headers = {'Content-Type': 'application/json'}

				external_request = requests.post(external_webhook_url, json=payload, headers=headers)  # send the post request to taskmanager webhook
				external_request.json()  # webhook response that we can send back to original request to this webhook

			return 'servers received', 200
		else:  # if IP address is not in whitelist return an unauthorized message/code
			return 'Unauthorized machine', 401
	except Exception as e:
		return f'Error: {str(e)}', 500  # return 500 (server error)


if __name__ == '__main__':
	app.run(debug=True)
