import re
import string
from collections import Counter
from pathlib import Path


def text_analyzer(file_path: str) -> dict:
    """
    Analyze a text file and return:
    1- Word count
    2- Sentence count
    3- Top 10 most frequent words (punctuation ignored)
    """

    # --- Validate file ---
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError("File not found.")

    # --- Read file ---
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    # --- Sentence count ---
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    sentence_count = len([s for s in sentences if s.strip()])
    sentence_count = len(sentences)

    # --- Print each sentence ---
    print("\n Sentences found:")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}. {sentence}")

    # --- Remove punctuation ---
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Word tokenization
    words = text.split()
    word_count = len(words)

    # --- Top 10 frequent words ---
    top_10_words = Counter(words).most_common(10)

    # --- Output ---
    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "top_10_words": top_10_words
    }


result = text_analyzer("sample_text.txt")

print("Word Count:", result["word_count"])
print("Sentence Count:", result["sentence_count"])
print("Top 10 Words:")
for word, freq in result["top_10_words"]:
    print(f"{word}: {freq}")
