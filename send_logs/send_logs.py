import re
from urllib.parse import urlparse, parse_qs
import requests

with open('../nginx/access.log', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for log_entry in lines:
    if "search" not in log_entry:
        continue
    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>[\w:/]+)\s[+\-]\d{4}\] '
        r'"(?P<method>\w+) (?P<path>[\S]+) HTTP/\d\.\d" (?P<status>\d+) \d+ "[^"]*" "[^"]*"'
    )

    # Применяем регулярное выражение к строке журнала
    match = log_pattern.match(log_entry)
    if match:
        ip_address = match.group('ip')
        date = match.group('date')
        path = match.group('path')
        status_code = int(match.group('status'))
        parsed_url = urlparse(path)
        endpoint = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        search_query = query_params.get('query', [None])[0]
        if search_query is None:
            search_query = query_params.get('search', [None])[0]

        t = requests.post("http://127.0.0.1:8000/add_log/", json={
            "search_query": search_query,
            "search_date": date,
            "search_ip": ip_address,
            "path": endpoint,
            "status_code": status_code
        })
        print(path)
        print(t.json())
