from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
	try:
		data = request.get_json()
		file_path = data.get('file')

		if file_path:
			print(file_path)
			result = subprocess.run(["cmd", "/c", file_path])

			print(result.stdout)
			return f'{file_path} executed successfully', 200
		else:
			return 'No file path provided', 400
	except Exception as e:
		return f'Error: {str(e)}', 500

if __name__ == '__main__':
	app.run(debug=True)
