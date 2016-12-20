'''
The application's entry point.
'''

import argparse
import sys
from crawllog.domains import domains


class Context:
    def __init__(self, args):
        self.lines = open(args.logfile, 'r')
        if args.out is not None:
            self.dest = open(args.out, 'w')
        else:
            self.dest = sys.stdout

    def write(self, *args):
        print(*args, file=self.dest)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.lines.close()
        if self.dest.close is not sys.stdout:
            self.dest.close()


def main():
    '''Setup API.'''
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='subcommands',
                                       description='Valid subcommands: domains',
                                       help='more help')

    parser_domains = subparsers.add_parser('urls-per-domain')
    parser_domains.add_argument('logfile', type=str, help='The crawl.log to process.')
    parser_domains.add_argument('--code', type=int, default=None,
                                help='Only count URLs for given response code.')
    parser_domains.add_argument('--out', default=None,
                                help='Only count URLs for given response code.')
    parser_domains.set_defaults(func=domains)

    args = parser.parse_args()

    with Context(args) as context:
        args.func(args, context)
