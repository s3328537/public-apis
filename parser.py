import json
import re

def parse_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    apis = []
    current_category = None

    # Regex to match a Markdown link [text](url)
    link_re = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    for line in lines:
        line = line.strip()

        # Check for category heading
        if line.startswith('### '):
            current_category = line[4:].strip()
            continue

        # Ignore lines before the first category
        if not current_category:
            continue

        # We only care about table rows
        if not line.startswith('|'):
            continue

        # Skip table header and separator rows
        # The user mentioned different table formattings, so let's be robust
        if re.search(r'\|\s*API\s*\|\s*Description\s*\|', line, re.IGNORECASE) or '|:---' in line:
            continue

        parts = line.split('|')

        # Depending on how the string was split, parts[0] is usually empty string and parts[-1] might be empty
        # Let's check we have at least 6 parts (1 before first |, 4 between |, 1 after last |) for 5 columns
        if len(parts) >= 6:
            parts = [p.strip() for p in parts]

            api_cell = parts[1]
            desc_cell = parts[2]
            auth_cell = parts[3]
            https_cell = parts[4]
            cors_cell = parts[5]

            # Extract API name and Link
            match = link_re.search(api_cell)
            if match:
                api_name = match.group(1).strip()
                api_link = match.group(2).strip()
                # Some links might have spaces inside the parentheses if malformed, but regex handles most
            else:
                api_name = api_cell.strip()
                api_link = ""

            # If the description contains multiple | it will break the split.
            # But standard markdown tables escape | or don't use them in cells.
            # Assuming standard tables.

            apis.append({
                "API": api_name,
                "Link": api_link,
                "Description": desc_cell,
                "Auth": auth_cell,
                "HTTPS": https_cell,
                "Cors": cors_cell,
                "Category": current_category
            })

    with open('public_apis.json', 'w', encoding='utf-8') as f:
        json.dump(apis, f, indent=2)

if __name__ == '__main__':
    parse_readme()
