#!/usr/bin/python
from __future__ import print_function
import argparse
import sys

from lib.crawllog import LogEntry


def omit_this(log_entry, response_code):
    return response_code is not None and not response_code == log_entry.response_code


def main(crawl_log, response_code, write=print):
    # Store log_entry as hash --> (occurences, urls)
    resources = dict()

    print('Parse log file ("%s")...' % crawl_log)
    with open(crawl_log, 'r') as src:
        for line in src:
            log_entry = LogEntry(line)
            if omit_this(log_entry, response_code):
                continue  # Omit any response code the user does not want
            if log_entry.hash in resources:
                resources[log_entry.hash][0] = resources[log_entry.hash][0] + 1
                resources[log_entry.hash][1].add(log_entry.url)
            else:
                resources[log_entry.hash] = [1, set([log_entry.url])]

    print('Write results')

    results = [resources[key] for key in resources]

    for data in sorted(results, key=lambda result: -result[0]):
        count = data[0]
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
    parser = argparse.ArgumentParser(prog='check-for-duplicates.py')
    parser.add_argument('crawl_log')
    parser.add_argument('-o', '--out', required=False)
    parser.add_argument('-c', '--code', required=False, type=int,
                        help='HTTP response code to filter before checking for duplicates.')

    options = parser.parse_args()

    if options.out:
        with open(options.out, 'w') as out:
            def write(line=''):
                out.write(line + '\n')
            main(options.crawl_log, options.code, write)
    else:
        main(options.crawl_log, options.code, print)
