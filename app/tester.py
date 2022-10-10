import re
import vertaler as vertaler

regexp = re.compile('[ ]')
test_string = 'moeder is een test'
vertaal = vertaler.laad_woorden()
print(vertaler.vertaal_zin(test_string, vertaal))
print('-------------------------------------------')
print(vertaler.leestekens(test_string, vertaal)[0])



