from unittest import TestCase, main
from unittest.mock import Mock

from lib.crawllog import extract_url, extract_response_code, LogEntry

LINE = '2016-04-30T10:53:40.583Z   200      23330 http://www.example.com/Team/123?detail ' + \
    'XLLLL http://www.example.com/other text/html #001 20160430105338145+2371 ' + \
    'sha1:ZOUAIUDUREKVOTUIVULTAQOFMCGVZEN3 SOURCE_TAG ANNOTATIONS'


class ExtractFieldsFromCrawllogTest(TestCase):
    def test_extract_url(self):
        self.assertEquals(extract_url(LINE), 'http://www.example.com/Team/123?detail')

    def test_extract_response_code(self):
        self.assertEquals(extract_response_code(LINE), '200')


class LogEntryTest(TestCase):
    def setUp(self):
        self.log_entry = LogEntry(LINE)

    def test_should_extract_timestamp(self):
        self.assertEquals('2016-04-30T10:53:40.583Z', self.log_entry.timestamp)

    def test_should_extract_response_code(self):
        self.assertEquals(200, self.log_entry.response_code)

    def test_should_extract_size(self):
        self.assertEquals('23330', self.log_entry.size)

    def test_should_extract_url(self):
        self.assertEquals('http://www.example.com/Team/123?detail', self.log_entry.url)

    def test_should_extract_mime(self):
        self.assertEquals('text/html', self.log_entry.mime)

    def test_should_extract_worker(self):
        self.assertEquals('#001', self.log_entry.worker)

    def test_should_extract_fetch_timestamp(self):
        self.assertEquals('20160430105338145+2371', self.log_entry.fetch_timestamp)

    def test_should_extract_hash(self):
        self.assertEquals('sha1:ZOUAIUDUREKVOTUIVULTAQOFMCGVZEN3', self.log_entry.hash)

    def test_should_extract_source_tag(self):
        self.assertEquals('SOURCE_TAG', self.log_entry.source_tag)

    def test_should_extract_annotations(self):
        self.assertEquals('ANNOTATIONS', self.log_entry.annotations)
