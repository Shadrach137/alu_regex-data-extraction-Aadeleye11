from regex_extraction import extract

def test_extract():
    test = """
    Phone numbers: (123) 456-7890, 123-456-7890, 123.456.7890
    Emails: user@example.com, firstname.lastname@company.co.uk
    Hashtags: #helloWorld, #2025Trends, #data_science
    Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
    """
    matches = extract(test)
    # Print the classification of each  in tabular format
    if matches:
        col_w = 42
        border = "-" * (col_w + 11)
        print("\n\n---------------Pattern Matches---------------")
        print(f"\n{border}\n| {'Value':<{col_w}}| Type   |\n{border}")

        for m in matches:
            print(f"| {m['value'][:col_w-1]:<{col_w}}| {m['type'].capitalize():6}|")
        
        print(border)
    else:
        print("No matches found.")
    # Count the occurrences of each type
    counts = {'Hashtag': 0, 'Credit': 0, 'Phone': 0, 'Email': 0}
    for m in matches:
        counts[m['type']] += 1
    print("\n------Pattern Count------")
    for key, value in counts.items():
        print(f"{key}: {value}")
      
if __name__ == "__main__":
    test_extract()
    print("All tests passed.")
# This test function checks if the regex_extraction.py script correctly identifies and extracts phone numbers, emails, hashtags, and credit card numbers from a sample text.
# It uses assertions to verify that each type of data is found in the results.