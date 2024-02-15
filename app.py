from flask import Flask
import unittest

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! This is the CICD using GitHub Actions" # added a line

class TestApp(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    def test_hello(self):
        response = self.tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

if __name__ == '__main__':
    # If the script is run directly, start the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    # If the script is imported, run the tests
    unittest.main()
