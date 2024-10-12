

def wordcount(text):
    words = text.split()
    return len(words)

def charcount(text):
    ccount = {}
    for char in text:
        c = char.lower()
        ccount[c] = ccount.get(c, 0) + 1
    return ccount


with open("books/frankenstein.txt") as f:
    text = f.read()
    wcount = wordcount(text)
    ccount = charcount(text)
    print(f"The text contains {wcount} words")
    for k, v in ccount.items():
        print(f"Character '{k}' was found {v} times")