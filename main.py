def main():
    bookPath = "books/frankenstein.txt"
    bookText = getText(bookPath) 
    wordCount = countWords(bookText)
    letterCount = countLetters(bookText)
    sortedCharsNums = sortCharsNums(letterCount)

    print()
    print()
    print()
    print(f"^^^^^^^^^^^^^Begin book report of {bookPath} ! ^^^^^^^^^^^^^")
    print(f"{wordCount} words were found in the book.")
    print()
    
    for item in sortedCharsNums:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]} was found {item["num"]} times.")

    print()
    print()
    print("^^^^^^^^^^^^^^ END ^^^^^^^^^^^^^^^")

def getText(path):
    with open(path) as t:
        return t.read()
    
def countWords(text):
    return len(text.split())

def countLetters(text):
    lowercaseText = text.lower()
    lettercount = {}

    for i in lowercaseText:
        if i in lettercount:
            lettercount[i] += 1
        else:
            lettercount[i] = 1
    return lettercount

def sortOn(dic):
    return dic["num"]


def sortCharsNums(charsNums):
    sortedDics =  []
    for cha in charsNums:
        sortedDics.append({"char": cha, "num": charsNums[cha]})
    sortedDics.sort(reverse=True, key=sortOn)
    return sortedDics



main()