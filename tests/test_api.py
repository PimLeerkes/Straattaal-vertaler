import unittest
import requests
import sys
sys.path.append('../')
import app.api as api

# Test voor de gewilde respons voor een woord zonder vertaling 
class TestCalc(unittest.TestCase):
    def test_api_string(self):
        message = {'message': 'xxx'}
        url = f'http://127.0.0.1:8000/nederlands/'
        result = requests.get(url, params=message)
        print(result.text)
        self.assertEqual(result.json(), {"vertaling": "xxx"}) 
