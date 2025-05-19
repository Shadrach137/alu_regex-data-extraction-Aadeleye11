# Regex Data Extraction

A zero-dependency Python script that **pulls hashtags, credit-card numbers, US/Canadian phone numbers, and email addresses from any text**—all through one tidy regular-expression pattern.

> **Repo:** `alu_regex-data-extraction-Aadeleye11`  
> **Author:** Aadeleye11 (African Leadership University)

---

## ✨ Features

| Pattern | Examples caught |
| ------- | --------------- |
| **Hashtag** | `#DataRocks` `#AI_2025` |
| **Credit card** | `1234-5678-9012-3456` `1234 5678 9012 3456` |
| **Phone Number** | `(123) 456-7890` `123-456-7890` `123.456.7890` |
| **Email Address** | `user@example.com` `first.last@uni.edu` |

* Accepts **file input** or **paste mode**—your choice.  
* Clear CLI (Command Line Interface) output: `type → value`.  
* Fully commented, beginner-friendly code (CS50-style).


## Edge Cases Handled
* Credit cards with dashes, spaces or none.
* Phone numbers with parentheses, dots, or dashes.
* Emails with subdomains, + tags, and mixed case.
* Hashtags up to 100 characters (letters/digits/underscores).

---
## 📕 Resources Used

* Harvard CS50 Regex Course
* GitHub Co-Pilot 

---
## 🔧 Prerequisites

* Python ≥ 3.8  
* Git (for cloning)

---

##  Testing

Run our lightweight test script to verify the extractor still hits all four pattern types:

```bash
python test_extract.py
```
---

## 🚀 Quick Start

```bash
# 1 – Clone your fork
git clone https://github.com/<YourUsername>/alu_regex-data-extraction-Aadeleye11.git
cd alu_regex-data-extraction-<YourUsername>

# 2 – Run with a text file
python regex_extractor.py -f sample.txt

# 3 – Or run and paste text, then send EOF (End of File), Ctrl + D for Linux and MacOS, Ctrl + Z for Windows and press ENTER
python regex_extractor.py

```
---

## 🧪 Sample Input and Result
### Test
```bash
    test = """
    Phone numbers: (123) 456-7890, 123-456-7890, 123.456.7890
    Emails: user@example.com, firstname.lastname@company.co.uk
    Hashtags: #helloWorld, #2025Trends, #data_science
    Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
    """
```
### Result
```bash
---------------Pattern Matches---------------

-----------------------------------------------------
| Value                                     | Type   |
-----------------------------------------------------
| (123) 456-7890                            | Phone |
| 123-456-7890                              | Phone |
| 123.456.7890                              | Phone |
| user@example.com                          | Email |
| firstname.lastname@company.co.uk          | Email |
| #helloWorld                               | Hashtag|
| #2025Trends                               | Hashtag|
| #data_science                             | Hashtag|
| 1234 5678 9012 3456                       | Credit|
| 1234-5678-9012-3456                       | Credit|
-----------------------------------------------------

------Pattern Count------
Hashtag: 3
Credit: 2
Phone: 3
Email: 2
All tests passed
```


