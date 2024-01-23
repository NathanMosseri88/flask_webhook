from flask import Flask, request
import subprocess
import os

app = Flask(__name__)


# when this endpoint is hit...
@app.route('/webhook', methods=['POST'])
def webhook():  # run this function.
	try:
		data = request.get_json()  # get the json body from request
		file = data.get('file')  # get the value of the key named file
		# create file path based on operating system - will use correct path separators for whatever system it is running on
		file_path = os.path.join(os.path.sep, 'Users', 'SimpleToWork', 'Desktop', 'New Projects', "Nathan's", 'webhook_testing', file)

		if os.path.exists(file_path):  # if the path exists
			print(file_path)
			result = subprocess.run(["cmd", "/c", file_path])  # run the file

			print(result.stdout)
			return f'{file_path} executed successfully', 200  # send successful response message/code
		else:
			return 'File not Found', 404  # 404 error if file not found
	except Exception as e:
		return f'Error: {str(e)}', 500  # return 500 (server error)


if __name__ == '__main__':
	app.run(debug=True)
