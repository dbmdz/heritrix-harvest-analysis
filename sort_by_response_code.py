#!/usr/bin/env python3

from __future__ import print_function
import argparse
import sys

from lib.collections import Collector
from lib.crawllog import extract_url, extract_response_code


def main(crawl_file, write):
    urls = Collector()
    with open(crawl_file, 'r') as source:
        for line in source:
            urls.add(extract_response_code(line), extract_url(line))

    for code in sorted(urls.collections):
        for url in sorted(urls.collections[code]):
            write("%s %s" % (code, url))
        write()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('crawl_log')
    # parser.add_argument('compare')
    parser.add_argument('-o', '--out', required=False)

    options = parser.parse_args()

    if options.out:
        with open(options.out, 'w') as out:
            def write(line=''):
                out.write(line + '\n')
            main(options.crawl_log, write)
    else:
        main(options.crawl_log, print)
