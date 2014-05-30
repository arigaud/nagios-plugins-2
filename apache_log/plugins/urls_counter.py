#!/usr/bin/env python
import sys
import logging
import os
import re

LOGGER = logging.getLogger(__name__)

class UrlsCounter():

    def __init__(self, outputFilePath):
        logging.info('creating UrlsCounter')
        self.outputFilePath = outputFilePath
        self.check_output_file()

    def check_output_file(self):
        if os.path.isfile(self.outputFilePath):
            LOGGER.info('file exist ' + self.outputFilePath)
        else:
            f = file(self.outputFilePath, "w")
            f.close()

    def stringFormatter(self, item, url):
        return '[' + item['date'] + ']  [AF_UrlRequestCount] ' + str(item['count']) + ' - ' + url + os.linesep

    def append_to_file(self, urls):
        if len(urls) > 0:
            f = file(self.outputFilePath, "a")
            for url in urls:
                s = self.stringFormatter(urls[url], url);
                #urls[url]['date'] + ' | ' + str(urls[url]['count']) + ' | ' + url + os.linesep
                LOGGER.info(s)
                f.write(s)

            f.close()




    def update(self, urls):
        urlsCount = {}

        if len(urls) > 0:

            for url in urls:
                if not url['url'] in urlsCount.keys():
                    urlsCount[url['url']] = {'date': url['date'], 'count': 1}
                else:
                    urlsCount[url['url']]['date'] = url['date']
                    urlsCount[url['url']]['count'] += 1

            self.append_to_file(urlsCount)

