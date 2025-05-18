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
* Clear CLI output: `type → value`.  
* Fully commented, beginner-friendly code (CS50-style).

---
## 📕 Resources Used

* Harvard CS50 Regex Course
* Git Co-Pilot 

---
## 🔧 Prerequisites

* Python ≥ 3.8  
* Git (for cloning)

---

## 🚀 Quick Start

```bash
# 1 – Clone your fork
git clone https://github.com/<YourUsername>/alu_regex-data-extraction-<YourUsername>.git
cd alu_regex-data-extraction-<YourUsername>

# 2 – Run with a text file
python regex_extractor.py -f sample.txt

# 3 – Or run and paste text, then send EOF
python regex_extractor.py

