def extract_url(line):
    parts = line.split()
    return parts[3]


def extract_response_code(line):
    parts = line.split()
    return parts[1]
