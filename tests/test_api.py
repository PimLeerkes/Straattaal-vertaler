import unittest
import requests
import sys
sys.path.append('../')

# Test voor de gewilde respons voor een woord zonder vertaling 
class TestCalc(unittest.TestCase):
    def test_api_string(self):
        message = {'message': 'xxx'}
        container = "172.17.0.2"
        url = f'http://{container}/nederlands/'
        result = requests.get(url, params=message)
        print(result.text)
        self.assertEqual(result.json(), {"vertaling": "xxx"}) 
