from regex_extraction import extract

def test_extract():
    test = """
    Phone numbers: (123) 456-7890, 123-456-7890, 123.456.7890
    Emails: user@example.com, firstname.lastname@company.co.uk
    Hashtags: #helloWorld, #2025Trends, #data_science
    Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
    """
    results = extract(test)
    # Print the classification of each match
    for r in results:
        print(f"Value: {r['value']}, Type: {r['type']}")
    # Check if the expected types are present
        
    types = [r['type'] for r in results]
    
    assert 'phone' in types, "Phone number not found"   
    assert 'email' in types, "Email not found"  
    assert 'hashtag' in types, "Hashtag not found"  
    assert 'credit' in types, "Credit card not found"
    
if __name__ == "__main__":
    test_extract()
    print("All tests passed.")
# This test function checks if the regex_extraction.py script correctly identifies and extracts phone numbers, emails, hashtags, and credit card numbers from a sample text.
# It uses assertions to verify that each type of data is found in the results.