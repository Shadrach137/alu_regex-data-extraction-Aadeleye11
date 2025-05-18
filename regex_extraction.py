import re
import sys
import argparse
from pathlib import Path

pattern = re.compile(
    r"(#\w+)|"                            # Hashtags
    r"(\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4})|"  # Credit cards
    r"(\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4})|"    # Phone numbers
    r"([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,63})",  # Emails
    re.IGNORECASE,
)

def extract(text):
    results = []
    for match in pattern.finditer(text):
        for i, group in enumerate(match.groups(), start=1):
            if group:
                types = ['hashtag', 'credit', 'phone', 'email']
                results.append({'type': types[i-1], 'value': group})
                break
    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=Path, help='File path')
    args = parser.parse_args()

    if args.file:
        text = args.file.read_text()
    else:
        file_path = input("Enter the path to a file (or press Enter to paste text): ").strip()
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        else:
            print("Paste text, then Ctrl-D (Unix) or Ctrl-Z (Windows):")
            text = sys.stdin.read()

    matches = extract(text)
    if matches:
        for m in matches:
            print(f"{m['type']}: {m['value']}")
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()
# This script extracts hashtags, credit card numbers, phone numbers, and email addresses from a given text.
# It uses regular expressions to identify these patterns and prints them out with their types.