'''
Creates a histogram of urls per domain.
'''

from crawllog.logfile import LogEntry


def domains(args, context):
    '''Count URLs for domains'''
    urls = dict()
    for line in context.lines:
        log_entry = LogEntry(line)
        domain = log_entry.domain()
        if domain is not None:
            if domain not in urls:
                urls[domain] = 0
            if args.code is None or args.code is log_entry.response_code:
                urls[domain] = urls.get(domain, 0) + 1
    for url in sorted(urls):
        context.write(url, '\t', urls[url])
