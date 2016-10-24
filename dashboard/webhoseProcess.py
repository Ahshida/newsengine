__author__ = 'Vignesh Prakasam'
import urllib2,json
import os
from django.conf import settings

class Process():

    def __init__(self):
        pass

    def crawling(self, val):
        print val
        response = urllib2.urlopen('https://webhose.io/search?token=762a6329-12e8-40b0-98ba-6063797006f6&format=json&q='+val)
        content = response.read()
        return content

    def decoding(self, content):
        resultSet = []
        j = json.loads(content)
        json_string = json.dumps(j, sort_keys=True, indent=2)
        # print json_string
        parent = j["posts"]
        urls = []
        titles = []
        i = 0
        for item in parent:
            urls.append(item["url"])
            titles.append(item["title"])
            i += 1
        # print urls
        # print texts
        # resultSet.append(urls)
        # resultSet.append(texts
        resultSet = zip(urls, titles)
        return resultSet
        # print resultSet[0].get(0)
        # for i in resultSet:
        #     print i.get(0)
        # return resultSet
        # obj = AlchemyConnect()
        # obj.entityExtraction(urls[34])

    def tempFile(self):
        filePath = os.path.join(settings.DASHBOARD_ROOT, 'jsonFile.txt')
        with open(filePath, 'r') as ft:
            data = ft.read()
        resultSet = []
        j = json.loads(data)
        json_string = json.dumps(j, sort_keys=True, indent=2)
        # print json_string
        parent = j["posts"]
        urls, titles, authors, organizations, dates, locations = [], [], [], [], [], []
        i = 0
        for item in parent:
            urls.append(item["url"])
            titles.append(item["thread"]["title"])
            authors.append(item["author"])
            organizations.append(item["organizations"])
            dates.append(item["published"])
            locations.append(item["locations"])
            i += 1
        print titles
        resultSet = zip(urls, titles, authors, organizations, dates, locations)
        return resultSet

    def processing(self, val):
        # content = self.crawling(val)
        # resultSet = self.decoding(content)
        resultSet = self.tempFile()
        return resultSet


p = Process()
p.processing("manchester United")