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


def main(crawl_file_reference, crawl_file_compare, write):
    '''
    Given two crawler log files, this method looks which URLs where downloaded in the reference
    (first log) to determine which one are missing in the second one.
    '''
    known_urls = set()

    print('Parse log file for comparison ("%s")...' % crawl_file_compare)
    with open(crawl_file_compare, 'r') as src:
        for line in src:
            known_urls.add(extract_url(line))

    missing_by_response_code = dict()

    print('Parse reference log file ("%s") and compare urls...' % crawl_file_reference)
    with open(crawl_file_reference, 'r') as src:
        for line in src:
            url = extract_url(line)
            if url not in known_urls:
                response_code = extract_response_code(line)
                if response_code not in missing_by_response_code:
                    missing_by_response_code[response_code] = []
                missing = missing_by_response_code[response_code]
                missing.append(url)

    print('Finished')

    for response_code in sorted(missing_by_response_code):
        write('Missing by response code %s:\n' % response_code)
        for url in missing_by_response_code[response_code]:
            write('\t' + url)
        write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='look-for-missing-urls.py')
    parser.add_argument('reference')
    parser.add_argument('compare')
    parser.add_argument('-o', '--out', required=False)

    options = parser.parse_args()

    if options.out:
        with open(options.out, 'w') as out:
            def write(line=''):
                out.write(line + '\n')
            main(options.reference, options.compare, write)
    else:
        main(options.reference, options.compare, print)
