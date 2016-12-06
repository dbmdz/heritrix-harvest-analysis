from crawllog.logfile import LogEntry


def domains(args):
    '''Count URLs for domains'''
    urls = dict()
    with open(args.logfile, 'r') as source:
        for line in source:
            log_entry = LogEntry(line)
            domain = log_entry.domain()
            if domain is not None:
                urls[domain] = urls.get(domain, 0) + 1
    for url in sorted(urls):
        print(url, '\t', urls[url])