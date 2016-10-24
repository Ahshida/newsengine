__author__ = 'Vignesh Prakasam'


from alchemyapi_python.alchemyapi import AlchemyAPI
import json
import os
from django.conf import settings


class AlchemyConnect:

    def __init__(self):
        pass

    def entityExtraction(self, url):
        # Create the AlchemyAPI Object
        alchemyapiObj = AlchemyAPI()

        print('')
        print('')
        print('############################################')
        print('#   Entity Extraction Example              #')
        print('############################################')
        print('')
        print('')

        print('Processing url: ', url)
        print('')

        response = alchemyapiObj.entities('url', url, {'sentiment': 1})

        if response['status'] == 'OK':
            print('## Response Object ##')
            print(json.dumps(response, indent=4))
            entityTreeMap = {}
            entityTreeMap["name"] = "entity"
            entityTreeMap["children"] = []
            print('')
            print('## Entities ##')
            for entity in response['entities']:
                sizeVal = float(entity['relevance']) * 100
                # self.positiveDict(entity)
                entityTreeMap["children"].append({"name": entity['text'].encode('utf-8'), "size": sizeVal})
                json_string = json.dumps(entityTreeMap, sort_keys=True, indent=2)
                print('text: ', entity['text'].encode('utf-8'))
                print('type: ', entity['type'])
                print('relevance: ', entity['relevance'])
                print('sentiment: ', entity['sentiment']['type'])
                if 'score' in entity['sentiment']:
                    print('sentiment score: ' + entity['sentiment']['score'])
                print('')
            print entityTreeMap
            print json.dumps(entityTreeMap, sort_keys=True, indent=2)
            file_path_write = os.path.join(settings.BASE_DIR, 'entity_current.json')
            with open(file_path_write, 'w') as fi:
                json.dump(entityTreeMap, fi, sort_keys=True, indent=2)

        else:
            print('Error in entity extraction call: ', response['statusInfo'])

al = AlchemyConnect()
al.entityExtraction("http://omgili.com/r/2wGaacqxAptJeDZf7TglbD3Tf19IsM7QucHA9IOYBWvVInSgLOkA_QREtCiSFfLMIBlhxAiBp89ic3ZCwoegVg--")

# entityTreeMap = {}
# entityTreeMap["name"] = "entity"
# entityTreeMap["children"] = []
# for i in xrange(0,5):
#     textMap = {"name": "sasdf", "size": i}
#     entityTreeMap["children"].append(textMap)
# print entityTreeMap
# json_string = json.dumps(entityTreeMap, sort_keys=True, indent=2)
# print json_string