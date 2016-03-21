#!/usr/bin/python
from __future__ import print_function
import argparse
import sys

class Info:
    def __init__(self, line):
        parts = line.split()
        self.timestamp = parts[0]
        self.response_code = int(parts[1])
        self.size = parts[2]
        self.url = parts[3]
        self.breadcrumb = parts[4]
        self.referrer = parts[5]
        self.mime = parts[6]
        self.worker = parts[7]
        self.fetch_timestamp = parts[8]
        self.hash = parts[9]
        self.source_tag = parts[10]
        self.annotations = parts[11]


def omit_this(info, response_code):
    return response_code is not None and not response_code == info.response_code


# def main2(crawl_log, response_code, write=print):
#     print('Parse log file for comparison ("%s")...' % crawl_log)

#     with open(crawl_log, 'r') as src:
#         resources = extract_resources(crawl_log, response_code)

#     print('Write results')
#     write_results(resources, write)

#     print('Finished.')


def main(crawl_log, response_code, write=print):
    # Store info as hash --> (occurences, urls)
    resources = dict()

    print('Parse log file ("%s")...' % crawl_log)
    with open(crawl_log, 'r') as src:
        for line in src:
            info = Info(line)
            if omit_this(info, response_code):
                continue # Omit any response code the user does not want
            if info.hash in resources:
                resources[info.hash][0] = resources[info.hash][0] + 1
                resources[info.hash][1].add(info.url)
            else:
                resources[info.hash] = [1, set([info.url])]

    print('Write results')

    results = [resources[key] for key in resources]

    for data in sorted(results, key=lambda result: -result[0]):
        count  = data[0]
        urls = data[1]
        if count > 1:
            first = True
            for url in sorted(urls):
                if first:
                    write('%d\t%s' % (count, url))
                    first = False
                else:
                    write('\t%s' % url)
            write()
    print('Finished.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog = 'check-for-duplicates.py')
    parser.add_argument('crawl_log')
    parser.add_argument('-o', '--out', required=False)
    parser.add_argument('-c', '--code', required=False, type=int, help='HTTP response code to filter before checking for duplicates.')

    options = parser.parse_args()

    if options.out:
        with open(options.out, 'w') as out:
            def write(line=''):
                out.write(line + '\n')
            main(options.crawl_log, options.code, write)
    else:
        main(options.crawl_log, options.code, print)
