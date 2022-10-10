import unittest
import requests
import sys
sys.path.append('../')
import re

import app.vertaler as vertaler

class Test_No_Spaces(unittest.TestCase):
    
    def test_vertaal(self):
        regexp = re.compile('[ ]')
        test_string = 'thisisatest'
        vertaal = vertaler.laad_woorden()
        self.assertFalse(bool(regexp.search(vertaal.vertaal(test_string))))
    
    def test_vertaal_zin(self):
        regexp = re.compile('[ ]')
        test_string = 'thisisatest'
        vertaal = vertaler.laad_woorden()
        print(vertaler.vertaal_zin(test_string, vertaal))
        self.assertFalse(bool(regexp.search(vertaler.vertaal_zin(test_string, vertaal))))
    
    def test_leestekens(self):
        regexp = re.compile('[ ]')
        test_string = 'thisisatest'
        vertaal = vertaler.laad_woorden()
        self.assertFalse(bool(regexp.search(vertaler.leestekens(test_string, vertaal)[0])))
