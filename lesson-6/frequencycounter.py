import os
import string
from collections import Counter

FILENAME = "sample.txt"
REPORT_FILE = "word_count_report.txt"

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

def count_words():
    if not os.path.exists(FILENAME):
        print("File not found. Please create 'sample.txt'.")
        return

    with open(FILENAME, "r") as file:
        text = file.read()

    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    
    word_count = Counter(words)

    total_words = sum(word_count.values())
    top_words = word_count.most_common(5)

    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

    with open(REPORT_FILE, "w") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write("Top 5 Words:\n")
        for word, count in top_words:
            report.write(f"{word} - {count}\n")

def main():
    count_words()

main()