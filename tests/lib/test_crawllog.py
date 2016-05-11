from unittest import TestCase, main
from unittest.mock import Mock

from lib.crawllog import extract_url, extract_response_code

LINE = '2016-04-30T10:53:34.917Z   200      28562 http://www.example.com/Team/123?detail text/html #002 20160430105332147+2703 sha1:U2UMURXQEWDWTHGYFSA4THMAINSA2U5F - -'

class ExtractFieldsFromCrawllogTest(TestCase):
    def test_extract_url(self):
        self.assertEquals(extract_url(LINE), 'http://www.example.com/Team/123?detail')

    def test_extract_response_code(self):
        self.assertEquals(extract_response_code(LINE), '200')
