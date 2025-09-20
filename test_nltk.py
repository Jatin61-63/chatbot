import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet

# Agar download pehle se ho gaya hai, toh ye load hona chahiye
def test_nltk():
    text = "Hello! My order hasn’t arrived yet. I want to track my order and check status."
    print("Original text:")
    print(text)
    
    # Sentence tokenization
    sentences = sent_tokenize(text)
    print("\nSentences:")
    for s in sentences:
        print("-", s)
    
    # Word tokenization
    words = word_tokenize(text)
    print("\nWords:")
    print(words)
    
    # WordNet: synonyms / definitions example
    w = "order"
    synsets = wordnet.synsets(w)
    print(f"\nSynsets of '{w}':")
    for syn in synsets[:3]:  # first 3 synsets
        print("Name:", syn.name())
        print("Definition:", syn.definition())
        print("Lemmas:", syn.lemma_names())
        print("---")

if __name__ == "__main__":
    test_nltk()
