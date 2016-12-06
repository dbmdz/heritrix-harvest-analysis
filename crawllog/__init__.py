'''
The application's entry point.
'''

import argparse
import sys
from crawllog.domains import domains

def main():
    '''Setup API.'''
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='subcommands',
                                       description='Valid subcommands: domains',
                                       help='more help')

    parser_domains = subparsers.add_parser('domains')
    parser_domains.add_argument('logfile', type=str, help='The crawl.log to process.')
    parser_domains.set_defaults(func=domains)

    args = parser.parse_args()
    args.func(args)
