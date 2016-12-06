def extract_url(line):
    parts = line.split()
    return parts[3]


def extract_response_code(line):
    parts = line.split()
    return parts[1]


class LogEntry:
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

    def domain(self):
        parts = self.url.split('/')
        if len(parts) > 1:
            return parts[2]
        else:
            return None
