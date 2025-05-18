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
    """
    Extracts hashtags, credit cards, phone numbers, and emails from the given text.
    """
    results = []
    for match in pattern.finditer(text):
        # Check which group matched and append to results
        for i, group in enumerate(match.groups(), start=1):
            if group:
                types = ['hastag', 'credit_card', 'phone_number', 'email']
                results.append({
                    'type': types[i-1],
                    'value': group,
                })
                break  # Only one group can match at a time
    return results

def main():
    parser = argparse.ArgumentParser(description="Extract hashtags, credit cards, phone numbers, and emails from text.")
    parser.add_argument(
        'input_file',
        type=Path,
        help="Path to the input text file."
    )
    args = parser.parse_args()
    
    if args.file:
        text = args.input_file.read_text()
    else:
        file_path = input("Enter the path to the text file or press Enter to paste text: ")
        if file_path:
            with open(file_path, 'r', encoding = 'utf-8') as file:
                text = file.read()
        else:
            print("Paste the text, then Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) to finish:")
            text = sys.stdin.read()
    
    matches = extract(text)
    if matches:
        for m in matches:
            print(f"{m['type']}: {m['value']}") 
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()
    # Check if the script is run directly

            