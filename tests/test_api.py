import unittest
import requests
import sys
sys.path.append('../')
import urllib.parse

class TestCalc(unittest.TestCase):
    def test_api_string(self):
        message = {'message': 'je moeder is niet cool'}
        url = f'http://127.0.0.1:8000/nederlands/'
        message = urllib.parse.urlencode(message)
        result = requests.get(url, params=message)
        print(result.text)
        self.assertEqual(result, {'vertaling': 'xxx'}) 
