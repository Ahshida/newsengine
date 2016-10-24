__author__ = 'U430p'

import json
from alchemyConnect import AlchemyConnect


with open('jsonFile.txt', 'r') as f:
    data = f.read()
j = json.loads(data)
json_string = json.dumps(j, sort_keys=True, indent=2)
# print json_string
parent = j["posts"]
urls = {}
i = 0
for item in parent:
    urls[i] = item["url"]
    i += 1
print urls[34]
obj = AlchemyConnect()
obj.entityExtraction(urls[34])