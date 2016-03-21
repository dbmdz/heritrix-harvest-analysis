#!/usr/bin/python
from __future__ import print_function
import argparse
import sys


def extract_url(line):
    parts = line.split()
    return parts[3]


def extract_response_code(line):
    parts = line.split()
    return parts[1]


def main(crawl_file, write):
    urls = dict()
    with open(crawl_file, 'r') as source:
        for line in source:
            code = extract_response_code(line)
            url = extract_url(line)
            if code in urls:
                urls[code].append(url)
            else:
                urls[code] = [url]

    for code in sorted(urls):
        for url in sorted(urls[code]):
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
