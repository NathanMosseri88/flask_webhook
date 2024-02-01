from flask import Flask, request, jsonify
import requests
import subprocess
import os
import json
from cryptography.fernet import Fernet
import ngrok

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
		requesting_ip = data.get('ip')

		if requesting_ip in WHITE_LIST:  # check if IP address in request is whitelisted

			servers = data.get('servers')  # list of server/username dicts
			print(servers)
			responses = []  # to log responses from external webhooks

			for server in servers:  # for each dict...

				# if ngrok subdomain routing is possible - builds on uniform URL idea
				# external_webhook_url = f'https://{server["Server Name"]}.exampleBaseDomain.com/{server["Username"]}'
				external_webhook_url = 'http://127.0.0.1:3000/manual_kickoff'

				payload = server  # request body with 'Server Name' and 'Username' dict
				headers = {'Content-Type': 'application/json'}

				# send the post request to taskmanager webhook
				external_request = requests.post(external_webhook_url, json=payload, headers=headers)

				# external response
				response = external_request.json()
				# add to array of responses from each webhook contacted
				responses.append(response)

			# return all responses back to client
			return f'{responses}', 200

		else:  # if IP address is not in whitelist return an unauthorized message/code
			return 'Unauthorized machine', 401

	except Exception as e:
		return f'delegation Error: {str(e)}', 500  # return 500 (server error)


if __name__ == '__main__':
	app.run(debug=True)
