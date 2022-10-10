import unittest
import requests
import sys
sys.path.append('../')
import app.api as api

class TestCalc(unittest.TestCase):
    def test_api_string(self):
        message = {'message': 'je moeder is niet cool'}
        url = f'http://127.0.0.1:8000/nederlands/'
        result = requests.get(url, params=message)
        print(result.text)
        self.assertEqual(result, {'vertaling': 'xxx'}) 
