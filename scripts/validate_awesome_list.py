#!/usr/bin/env python3

import re
import sys
from pathlib import Path

root = Path.cwd()
files = []
for entry in root.iterdir():
    if entry.is_file() and entry.suffix.lower() == '.md':
        if entry.name not in {'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md'}:
            files.append(entry.name)

entries = []
errors = []
pattern = re.compile(r'^- \*\*\[([^\]]+)\]\(([^)]+)\)\*\* - (.+)$')

for file_name in sorted(files):
    file_path = root / file_name
    text = file_path.read_text(encoding='utf-8')

    for line_number, line in enumerate(text.splitlines(), start=1):
        match = pattern.match(line)
        if not match:
            continue

        title, url, description = match.groups()
        normalized_title = title.strip()
        normalized_url = url.strip()
        cleaned_description = description.strip()

        if not cleaned_description.endswith('.'):
            errors.append(f'{file_name}:{line_number} - Description for "{normalized_title}" does not end with a period.')

        if not re.match(r'^https?://', normalized_url) and not normalized_url.startswith('.') and not re.fullmatch(r'[A-Za-z0-9._/\-]+\.md', normalized_url):
            errors.append(f'{file_name}:{line_number} - URL for "{normalized_title}" is not a valid external URL or repo-relative file path: {normalized_url}')

        entries.append({
            'file_name': file_name,
            'title': normalized_title,
            'url': normalized_url,
            'line_number': line_number,
        })

title_map = {}
url_map = {}
for entry in entries:
    title_key = (entry['file_name'], entry['title'].lower())
    if title_key in title_map:
        first = title_map[title_key]
        errors.append(f'Duplicate title found: "{entry["title"]}" in {entry["file_name"]}:{entry["line_number"]} matches {first["file_name"]}:{first["line_number"]}.')
    else:
        title_map[title_key] = entry

    url_key = (entry['file_name'], entry['url'].lower())
    if url_key in url_map:
        first = url_map[url_key]
        errors.append(f'Duplicate URL found: {entry["url"]} in {entry["file_name"]}:{entry["line_number"]} matches {first["file_name"]}:{first["line_number"]}.')
    else:
        url_map[url_key] = entry

if errors:
    print('Awesome list validation failed.')
    for error in errors:
        print(f'- {error}')
    raise SystemExit(1)

print(f'Validated {len(entries)} resource entries across {len(files)} markdown files.')
