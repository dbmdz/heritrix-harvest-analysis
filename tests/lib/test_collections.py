from unittest import TestCase, main
from unittest.mock import Mock

from lib.collections import Collector


class CollectorTest(TestCase):
    def test_collect_should_create_new_groups(self):
        collector = Collector()
        collector.add('Test', None)
        self.assertEquals(len(collector.collections), 1)

    def test_collect_should_add_value_to_group(self):
        collector = Collector()
        collector.add('Test', 'ABCDEF')
        self.assertTrue('ABCDEF' in collector.collections['Test'])
